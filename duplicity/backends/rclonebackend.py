# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2019 Francesco Magno
# Copyright 2019 Kenneth Loafman <kenneth@loafman.com>
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

from future import standard_library
standard_library.install_aliases()
from builtins import str
from builtins import range
from builtins import object

import os
import os.path

import duplicity.backend
from duplicity import path
from duplicity import log
from duplicity.errors import BackendException
from duplicity import util


class RcloneBackend(duplicity.backend.Backend):

    def __init__(self, parsed_url):
        duplicity.backend.Backend.__init__(self, parsed_url)
        self.rclone_cmd = u"rclone"
        self.parsed_url = parsed_url
        self.remote_path = self.parsed_url.path

        try:
            rc, o, e = self.subprocess_popen(
                self.rclone_cmd + u" --version")
        except Exception:
            log.FatalError(u"rclone not found: please install rclone", log.ErrorCode.backend_error)

        if parsed_url.path.startswith(u"//"):
            self.remote_path = self.remote_path[2:].replace(u":/", u":", 1)

        self.remote_path = util.fsdecode(self.remote_path)

    def _get(self, remote_filename, local_path):
        remote_filename = util.fsdecode(remote_filename)
        local_pathname = util.fsdecode(local_path.name)
        temp_dir = os.path.dirname(local_pathname)
        commandline = u"%s copy %s/%s %s" % (
            self.rclone_cmd, self.remote_path, remote_filename, temp_dir)
        rc, o, e = self.subprocess_popen(commandline)
        if rc != 0:
            if os.path.isfile(os.path.join(temp_dir, remote_filename)):
                os.remove(os.path.join(temp_dir, remote_filename))
            raise BackendException(e.split(u'\n')[0])
        os.rename(os.path.join(temp_dir, remote_filename), local_pathname)

    def _put(self, source_path, remote_filename):
        source_pathname = util.fsdecode(source_path.name)
        remote_filename = util.fsdecode(remote_filename)
        temp_dir = util.fsdecode(os.path.dirname(source_pathname))
        temp_filename = os.path.basename(source_pathname)
        os.rename(source_pathname, os.path.join(temp_dir, remote_filename))
        commandline = u"%s copy --include %s %s %s" % (
            self.rclone_cmd, remote_filename, temp_dir, self.remote_path)
        rc, o, e = self.subprocess_popen(commandline)
        if rc != 0:
            os.rename(os.path.join(temp_dir, remote_filename), source_pathname)
            raise BackendException(e.split(u'\n')[0])
        os.rename(os.path.join(temp_dir, remote_filename), source_pathname)

    def _list(self):
        filelist = []
        commandline = u"%s ls %s" % (
            self.rclone_cmd, self.remote_path)
        rc, o, e = self.subprocess_popen(commandline)
        if rc != 0:
            if e.endswith(u"not found\n"):
                return filelist
            else:
                raise BackendException(e.split(u'\n')[0])
        if not o:
            return filelist
        return [util.fsencode(x.split()[-1]) for x in o.split(u'\n') if x]

    def _delete(self, remote_filename):
        remote_filename = util.fsdecode(remote_filename)
        commandline = u"%s delete --drive-use-trash=false --include %s %s" % (
            self.rclone_cmd, remote_filename, self.remote_path)
        rc, o, e = self.subprocess_popen(commandline)
        if rc != 0:
            raise BackendException(e.split(u'\n')[0])


duplicity.backend.register_backend(u"rclone", RcloneBackend)
