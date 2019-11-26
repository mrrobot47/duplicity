# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2002 Ben Escoto <ben@emerose.org>
# Copyright 2007 Kenneth Loafman <kenneth@loafman.com>
# Copyright 2019 Carl Adams <carlalex@overlords.com>
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

from __future__ import division
import os
import time

import duplicity.backend
from duplicity import log
from duplicity.errors import FatalBackendException, BackendException
from duplicity import util

# Note: current gaps with the old boto backend include:
#       - no "multi" support yet.
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
        self.resetConnection()

    def resetConnection(self):
        # The older "boto" backend would try to create buckets here
        # if they did not exist. We are currently not doing this
        # for a couple of reasons: 1) doing it here would result
        # in bucket creation when doing a status check on a
        # non-existing backup or bucket, and 2) it's probably not a
        # great practice to give any automated backup process
        # bucket creation permissions.  Not performing bucket
        # creation also simplifies region handling.

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

        self.bucket = self.s3.Bucket(self.bucket_name) # only set if bucket is thought to exist.

    def _put(self, source_path, remote_filename):
        remote_filename = util.fsdecode(remote_filename)

        key = self.key_prefix + remote_filename

        # TODO: old feature not yet implemented: CLI controlled storage class,
        # with manifest exempt from glacier.
        storage_class = u'STANDARD'
        log.Info(u"Uploading %s/%s to %s Storage" % (self.straight_url, remote_filename, storage_class))

        upload_start = time.time()
        self.s3.Object(self.bucket.name, key).upload_file(source_path.uc_name)
        upload_end = time.time()

        total_s = abs(upload_end - upload_start) or 1  # prevent a zero value!
        rough_upload_speed = os.path.getsize(source_path.name) / total_s
        log.Debug(u"Uploaded %s/%s to %s Storage at roughly %f bytes/second" %
                  (self.straight_url, remote_filename, storage_class,
                   rough_upload_speed))

    def _get(self, remote_filename, local_path):
        remote_filename = util.fsdecode(remote_filename)
        key = self.key_prefix + remote_filename
        # self.pre_process_download(remote_filename, wait=True) # XXX Not yet implemented for boto3
        self.s3.Object(self.bucket.name, key).download_file(local_path.uc_name)

    def _list(self):
        filename_list = []
        for obj in self.bucket.objects.filter(Prefix=self.key_prefix):
            #  .list(prefix=self.key_prefix):
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
        remote_filename = util.fsdecode(remote_filename)
        key = self.key_prefix + remote_filename
        content_length = self.s3.Object(self.bucket.name, key).content_length
        return {u'size': content_length}
