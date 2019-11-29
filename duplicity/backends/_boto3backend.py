# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2002 Ben Escoto <ben@emerose.org>
# Copyright 2007 Kenneth Loafman <kenneth@loafman.com>
# Copyright 2019 Carl A. Adams <carlalex@overlords.com>
#
# This file is part of duplicity.
#
# Duplicity is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# Duplicity is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with duplicity; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA

import duplicity.backend
from duplicity import log
from duplicity.errors import FatalBackendException, BackendException
from duplicity import util
from duplicity import progress


# Note: current gaps with the old boto backend include:
#       - no built in retries (rely on caller's retry, so won't fix)
#       - no support for a hostname/port in S3 URL yet.
#       - global.s3_unencrypted_connection unsupported (won't fix?)
#       - Not supporting older style buckets. (Won't fix)
#       - Not currently supporting bucket creation
#           - Makes the "european bucket" options obsolete
#           - TBD if this should be supported. I personally
#             feel that bucket creation is out of scope.
#             The old code would create a bucket if you simply
#             tried to stat a non-existing bucket/backup.
#             I also think it's poor separation of privileges
#             to give your backup credentials bucket creation
#             rights.
#       - Storage classes not yet supported
#             global.s3_use_rrs
#             global.s3_use_onezone_ia
#             global.s3_use_ia
#             global.s3_use_glacier
#       - Server side encryption not yet supported
#             globals.s3_use_sse
#             globals.s3_user_sse_kms
#             globals.s3_kms_key_id
#             globals.s3_lms_grant
#        - Glacier restore to S3 not yet implemented.
#        - No retry implemented in put. Is duplicity's retry enough?
#          must we do this in the backend?)
# TODO: New feature, not in old impl: when restoring from glacier or deep
#       archive, specify TTL.
# TODO: New feature, not in old impl: if restoring from glacier/deep archive,
#       allow user to specify how fast to restore (impacts cost).
# TODO: Update docs
# Note: I'm not sure if initiating glacier restores should be in scope.
#       Waiting on them (as was done) can be days. But, large restores can
#       be days too.

class BotoBackend(duplicity.backend.Backend):
    u"""
    Backend for Amazon's Simple Storage System, (aka Amazon S3), though
    the use of the boto3 module. (See
    https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
    for information on boto3.)
.
    Pursuant to Amazon's announced deprecation of path style S3 access,
    this backend only supports virtual host style bucket URIs.

    FIXME: document how boto3 gets creds
    To make use of this backend you must set aws_access_key_id
    and aws_secret_access_key in your ~/.boto or /etc/boto.cfg
    with your Amazon Web Services key id and secret respectively.
    Alternatively you can export the environment variables
    AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.
    """

    def __init__(self, parsed_url):
        duplicity.backend.Backend.__init__(self, parsed_url)

        # This folds the null prefix and all null parts, which means that:
        #  //MyBucket/ and //MyBucket are equivalent.
        #  //MyBucket//My///My/Prefix/ and //MyBucket/My/Prefix are equivalent.
        url_path_parts = [x for x in parsed_url.path.split(u'/') if x != u'']
        if url_path_parts:
            self.bucket_name = url_path_parts.pop(0)
        else:
            raise BackendException(u'S3 requires a bucket name.')

        if url_path_parts:
            self.key_prefix = u'%s/' % u'/'.join(url_path_parts)
        else:
            self.key_prefix = u''

        self.parsed_url = parsed_url
        self.straight_url = duplicity.backend.strip_auth_from_url(parsed_url)
        self.s3 = None
        self.bucket = None
        self.tracker = UploadProgressTracker()
        self.resetConnection()

    def resetConnection(self):
        import boto3
        import botocore
        from botocore.exceptions import ClientError

        self.bucket = None
        self.s3 = boto3.resource('s3')

        try:
            self.s3.meta.client.head_bucket(Bucket=self.bucket_name)
        except botocore.exceptions.ClientError as bce:
            error_code = bce.response['Error']['Code']
            if error_code == '404':
                raise FatalBackendException(u'S3 bucket "%s" does not exist' % self.bucket_name,
                                            code=log.ErrorCode.backend_not_found)
            else:
                raise

        self.bucket = self.s3.Bucket(self.bucket_name)  # only set if bucket is thought to exist.

    def _put(self, local_source_path, remote_filename):
        remote_filename = util.fsdecode(remote_filename)
        key = self.key_prefix + remote_filename
        # TODO: old feature not yet implemented: CLI controlled storage class,
        # with manifest exempt from glacier.
        storage_class = u'STANDARD'
        log.Info(u"Uploading %s/%s to %s Storage" % (self.straight_url, remote_filename, storage_class))
        # Should the tracker be scoped to the put or the backend?
        # The put seems right to me, but the results look a little more correct
        # scoped to the back-end.  This brings up questions about knowing when
        # it's proper for it to be reset.
        # tracker = UploadProgressTracker() # Scope the tracker to the put()
        tracker = self.tracker
        self.s3.Object(self.bucket.name, key).upload_file(local_source_path.uc_name, Callback=tracker.progress_cb)

    def _get(self, remote_filename, local_path):
        remote_filename = util.fsdecode(remote_filename)
        key = self.key_prefix + remote_filename
        self.s3.Object(self.bucket.name, key).download_file(local_path.uc_name)

    def _list(self):
        filename_list = []
        for obj in self.bucket.objects.filter(Prefix=self.key_prefix):
            try:
                filename = obj.key.replace(self.key_prefix, u'', 1)
                filename_list.append(filename)
                log.Debug(u"Listed %s/%s" % (self.straight_url, filename))
            except AttributeError:
                pass
        return filename_list

    def _delete(self, remote_filename):
        remote_filename = util.fsdecode(remote_filename)
        key = self.key_prefix + remote_filename
        self.s3.Object(self.bucket.name, key).delete()

    def _query(self, remote_filename):
        import botocore
        from botocore.exceptions import ClientError

        remote_filename = util.fsdecode(remote_filename)
        key = self.key_prefix + remote_filename
        content_length = -1
        try:
            s3_obj = self.s3.Object(self.bucket.name, key)
            s3_obj.load()
            content_length = s3_obj.content_length
        except botocore.exceptions.ClientError as bce:
            if bce.response['Error']['Code'] == '404':
                pass
            else:
                raise
        return {u'size': content_length}


class UploadProgressTracker(object):
    def __init__(self):
        self.total_bytes = 0

    def progress_cb(self, fresh_byte_count):
        self.total_bytes += fresh_byte_count
        progress.report_transfer(self.total_bytes, 0)  # second arg appears to be unused
        # It would seem to me that summing progress should be the callers job,
        # and backends should just toss bytes written numbers over the fence.
        # But, the progress bar doesn't work in a reasonable way when we do
        # that. (This would also eliminate the need for this class to hold
        # the scoped rolling total.)
        # progress.report_transfer(fresh_byte_count, 0)
