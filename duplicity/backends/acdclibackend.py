# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2015 Stefan Breunig <stefan-duplicity@breunig.xyz>
# Copyright 2015 Malay Shah <malays@gmail.com>
# Based on the backend ncftpbackend.py
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

import os.path
import urllib
import string
import json

import duplicity.backend
from duplicity import globals
from duplicity import log
from duplicity.errors import *  # @UnusedWildImport
from duplicity import tempdir


class ACDBackend(duplicity.backend.Backend):
    acd_cmd = u'acd_cli'
    u"""Connect to remote store using acd_cli"""
    def __init__(self, parsed_url):
        duplicity.backend.Backend.__init__(self, parsed_url)

        # we expect an error return, so go low-level and ignore it
        try:
            p = os.popen(self.acd_cmd + u" version")
            fout = p.read()
            ret = p.close()
        except Exception:
            pass
        # the expected error is 0
        if ret is not None:
            log.FatalError(self.acd_cmd + u" not found:  Please install acd_cli",
                           log.ErrorCode.backend_not_found)

        self.parsed_url = parsed_url
        self.url_string = duplicity.backend.strip_auth_from_url(self.parsed_url)

        # Use an explicit directory name.
        if self.url_string[-1] != u'/':
            self.url_string += u'/'

        self.subprocess_popen(self.acd_cmd + u" sync")

        # Initialize remote directory
        remote_path = urllib.unquote(self.parsed_url.path.replace(u'///', u'/')).rstrip()
        commandline = self.acd_cmd + u" ls '%s'" % (remote_path)
        try:
            self.subprocess_popen(commandline)
        except BackendException as e:
            if e.code == 50:  # Remote directory not there, create a new one
                commandline = self.acd_cmd + u" mkdir '%s'" % remote_path
                self.subprocess_popen(commandline)

    def _put(self, source_path, remote_filename=None):
        u"""Transfer source_path to remote_filename"""
        if not remote_filename:
            remote_filename = source_path.get_filename()

        # WORKAROUND for acd_cli: cannot specify remote filename
        # Link tmp file to the desired remote filename locally and upload
        remote_path = urllib.unquote(self.parsed_url.path.replace(u'///', u'/'))
        local_real_duplicity_file = os.path.join(os.path.dirname(source_path.name), remote_filename.rstrip())

        deleteFile = False
        if(source_path.name != local_real_duplicity_file):
            try:
                os.symlink(source_path.name, local_real_duplicity_file)
                deleteFile = True
            except IOError as e:
                log.FatalError(u"Unable to copy " + source_path.name + u" to " + local_real_duplicity_file)

        commandline = self.acd_cmd + u" upload --force --overwrite '%s' '%s'" % \
            (local_real_duplicity_file, remote_path)

        try:
            l = self.subprocess_popen(commandline)
        finally:
            if (deleteFile):
                try:
                    os.remove(local_real_duplicity_file)
                except OSError as e:
                    log.FatalError(u"Unable to remove file %s" % e)

    def _get(self, remote_filename, local_path):
        u"""Get remote filename, saving it to local_path"""
        remote_path = os.path.join(urllib.unquote(self.parsed_url.path.replace(u'///', u'/')), remote_filename).rstrip()
        local_dir = os.path.dirname(local_path.name)
        local_filename = os.path.basename(local_path.name)
        commandline = self.acd_cmd + u" download '%s' '%s'" % \
            (remote_path, local_dir)
        l = self.subprocess_popen(commandline)

        # Keep the remote filename and move the file over
        try:
            os.rename(os.path.join(local_dir, remote_filename), local_path.name)
        except IOError as e:
            log.FatalError(u"Unable to move file %s" % e)

        local_path.setdata()
        if not local_path.exists():
            raise BackendException(u"File %s not found" % local_path.name)

    def _query(self, remote_filename):
        remote_path = os.path.join(urllib.unquote(self.parsed_url.path.replace(u'///', u'/')), remote_filename).rstrip()
        commandline = self.acd_cmd + u" metadata '%s'" % remote_path
        node = self.subprocess_popen(commandline)
        if (node[0] == 0 and node[1]):
            try:
                size = json.loads(node[1])[u'contentProperties'][u'size']
                return {u'size': size}
            except ValueError as e:
                raise BackendException(u'Malformed JSON: expected "contentProperties->size" member in %s' % node[1])
        return {u'size': -1}

    def _list(self):
        u"""List files in directory"""
        def dir_split(str):
            if (str):
                return str.split()[2]
            else:
                return None
        commandline = self.acd_cmd + u" ls '%s'" % self.parsed_url.path.replace(u'///', u'/')
        l = self.subprocess_popen(commandline)
        return [x for x in map(dir_split, l[1].split(u'\n')) if x]

    def _delete(self, remote_filename):
        u"""Delete remote_filename"""
        remote_file_path = os.path.join(urllib.unquote(self.parsed_url.path.replace(u'///', u'/')),
                                        remote_filename).rstrip()
        commandline = self.acd_cmd + u" rm '%s'" % (remote_file_path)
        self.subprocess_popen(commandline)


duplicity.backend.register_backend(u"acd+acdcli", ACDBackend)
