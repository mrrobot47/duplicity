from __future__ import print_function
# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
# vim:tabstop=4:shiftwidth=4:expandtab
#
# Copyright 2014 Google Inc.
# Contact Michael Stapelberg <stapelberg+duplicity@google.com>
# This is NOT a Google product.
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

import time
import json
import os
import sys

import duplicity.backend
from duplicity.errors import BackendException
from duplicity import globals
from duplicity import log

# For documentation on the API, see
# http://msdn.microsoft.com/en-us/library/dn659752.aspx
# http://msdn.microsoft.com/en-us/library/dn631844.aspx
# https://gist.github.com/rgregg/37ba8929768a62131e85


class OneDriveBackend(duplicity.backend.Backend):
    u"""Uses Microsoft OneDrive (formerly SkyDrive) for backups."""

    OAUTH_TOKEN_PATH = os.path.expanduser(
        u'~/.duplicity_onedrive_oauthtoken.json')

    API_URI = u'https://apis.live.net/v5.0/'
    MAXIMUM_FRAGMENT_SIZE = 60 * 1024 * 1024
    BITS_1_5_UPLOAD_PROTOCOL = u'{7df0354d-249b-430f-820d-3d2a9bef4931}'
    CLIENT_ID = u'000000004C12E85D'
    CLIENT_SECRET = u'k1oR0CbtbvTG9nK1PEDeVW2dzvAaiN4d'
    OAUTH_TOKEN_URI = u'https://login.live.com/oauth20_token.srf'
    OAUTH_AUTHORIZE_URI = u'https://login.live.com/oauth20_authorize.srf'
    OAUTH_REDIRECT_URI = u'https://login.live.com/oauth20_desktop.srf'
    # wl.skydrive is for reading files,
    # wl.skydrive_update is for creating/writing files,
    # wl.offline_access is necessary for duplicity to access onedrive without
    # the user being logged in right now.
    OAUTH_SCOPE = [u'wl.skydrive', u'wl.skydrive_update', u'wl.offline_access']

    def __init__(self, parsed_url):
        duplicity.backend.Backend.__init__(self, parsed_url)

        # Import requests and requests-oauthlib
        try:
            # On debian (and derivatives), get these dependencies using:
            # apt-get install python-requests python-requests-oauthlib
            # On fedora (and derivatives), get these dependencies using:
            # yum install python-requests python-requests-oauthlib
            global requests
            global OAuth2Session
            import requests
            from requests_oauthlib import OAuth2Session
        except ImportError as e:
            raise BackendException((
                u'OneDrive backend requires python-requests and '
                u'python-requests-oauthlib to be installed. Please install '
                u'them and try again.\n' + str(e)))

        self.names_to_ids = None
        self.user_id = None
        self.directory = parsed_url.path.lstrip(u'/')
        if self.directory == u"":
            raise BackendException((
                u'You did not specify a path. '
                u'Please specify a path, e.g. onedrive://duplicity_backups'))
        if globals.volsize > (10 * 1024 * 1024 * 1024):
            raise BackendException((
                u'Your --volsize is bigger than 10 GiB, which is the maximum '
                u'file size on OneDrive.'))
        self.initialize_oauth2_session()
        self.resolve_directory()

    def initialize_oauth2_session(self):
        def token_updater(token):
            try:
                with open(self.OAUTH_TOKEN_PATH, u'w') as f:
                    json.dump(token, f)
            except Exception as e:
                log.Error((u'Could not save the OAuth2 token to %s. '
                           u'This means you may need to do the OAuth2 '
                           u'authorization process again soon. '
                           u'Original error: %s' % (
                               self.OAUTH_TOKEN_PATH, e)))

        token = None
        try:
            with open(self.OAUTH_TOKEN_PATH) as f:
                token = json.load(f)
        except IOError as e:
            log.Error((u'Could not load OAuth2 token. '
                       u'Trying to create a new one. (original error: %s)' % e))

        self.http_client = OAuth2Session(
            self.CLIENT_ID,
            scope=self.OAUTH_SCOPE,
            redirect_uri=self.OAUTH_REDIRECT_URI,
            token=token,
            auto_refresh_kwargs={
                u'client_id': self.CLIENT_ID,
                u'client_secret': self.CLIENT_SECRET,
            },
            auto_refresh_url=self.OAUTH_TOKEN_URI,
            token_updater=token_updater)

        # We have to refresh token manually because it's not working "under the covers"
        if token is not None:
            self.http_client.refresh_token(self.OAUTH_TOKEN_URI)

        # Send a request to make sure the token is valid (or could at least be
        # refreshed successfully, which will happen under the covers). In case
        # this request fails, the provided token was too old (i.e. expired),
        # and we need to get a new token.
        user_info_response = self.http_client.get(self.API_URI + u'me')
        if user_info_response.status_code != requests.codes.ok:
            token = None

        if token is None:
            if not sys.stdout.isatty() or not sys.stdin.isatty():
                log.FatalError((u'The OAuth2 token could not be loaded from %s '
                                u'and you are not running duplicity '
                                u'interactively, so duplicity cannot possibly '
                                u'access OneDrive.' % self.OAUTH_TOKEN_PATH))
            authorization_url, state = self.http_client.authorization_url(
                self.OAUTH_AUTHORIZE_URI, display=u'touch')

            print()
            print(u'In order to authorize duplicity to access your OneDrive, '
                  u'please open %s in a browser and copy the URL of the blank '
                  u'page the dialog leads to.' % authorization_url)
            print()

            redirected_to = raw_input(u'URL of the blank page: ').strip()

            token = self.http_client.fetch_token(
                self.OAUTH_TOKEN_URI,
                client_secret=self.CLIENT_SECRET,
                authorization_response=redirected_to)

            user_info_response = self.http_client.get(self.API_URI + u'me')
            user_info_response.raise_for_status()

            try:
                with open(self.OAUTH_TOKEN_PATH, u'w') as f:
                    json.dump(token, f)
            except Exception as e:
                log.Error((u'Could not save the OAuth2 token to %s. '
                           u'This means you need to do the OAuth2 authorization '
                           u'process on every start of duplicity. '
                           u'Original error: %s' % (
                               self.OAUTH_TOKEN_PATH, e)))

        if u'id' not in user_info_response.json():
            log.Error(u'user info response lacks the "id" field.')

        self.user_id = user_info_response.json()[u'id']

    def resolve_directory(self):
        u"""Ensures self.directory_id contains the folder id for the path.

        There is no API call to resolve a logical path (e.g.
        /backups/duplicity/notebook/), so we recursively list directories
        until we get the object id of the configured directory, creating
        directories as necessary.
        """
        object_id = u'me/skydrive'
        for component in [x for x in self.directory.split(u'/') if x]:
            tried_mkdir = False
            while True:
                files = self.get_files(object_id)
                names_to_ids = {x[u'name']: x[u'id'] for x in files}
                if component not in names_to_ids:
                    if not tried_mkdir:
                        self.mkdir(object_id, component)
                        tried_mkdir = True
                        continue
                    raise BackendException((
                        u'Could not resolve/create directory "%s" on '
                        u'OneDrive: %s not in %s (files of folder %s)' % (
                            self.directory, component,
                            names_to_ids.keys(), object_id)))
                break
            object_id = names_to_ids[component]
        self.directory_id = object_id
        log.Debug(u'OneDrive id for the configured directory "%s" is "%s"' % (
            self.directory, self.directory_id))

    def mkdir(self, object_id, folder_name):
        data = {u'name': folder_name, u'description': u'Created by duplicity'}
        headers = {u'Content-Type': u'application/json'}
        response = self.http_client.post(
            self.API_URI + object_id,
            data=json.dumps(data),
            headers=headers)
        response.raise_for_status()

    def get_files(self, path):
        response = self.http_client.get(self.API_URI + path + u'/files')
        response.raise_for_status()
        if u'data' not in response.json():
            raise BackendException((
                u'Malformed JSON: expected "data" member in %s' % (
                    response.json())))
        return response.json()[u'data']

    def _list(self):
        files = self.get_files(self.directory_id)
        self.names_to_ids = {x[u'name']: x[u'id'] for x in files}
        return [x[u'name'] for x in files]

    def get_file_id(self, remote_filename):
        u"""Returns the file id from cache, updating the cache if necessary."""
        if (self.names_to_ids is None or
                remote_filename not in self.names_to_ids):
            self._list()
        return self.names_to_ids.get(remote_filename)

    def _get(self, remote_filename, local_path):
        with local_path.open(u'wb') as f:
            file_id = self.get_file_id(remote_filename)
            if file_id is None:
                raise BackendException((
                    u'File "%s" cannot be downloaded: it does not exist' % (
                        remote_filename)))
            response = self.http_client.get(
                self.API_URI + file_id + u'/content', stream=True)
            response.raise_for_status()
            for chunk in response.iter_content(chunk_size=4096):
                if chunk:
                    f.write(chunk)
            f.flush()

    def _put(self, source_path, remote_filename):
        # Check if the user has enough space available on OneDrive before even
        # attempting to upload the file.
        source_size = os.path.getsize(source_path.name)
        start = time.time()
        response = self.http_client.get(self.API_URI + u'me/skydrive/quota')
        response.raise_for_status()
        if (u'available' in response.json() and
                source_size > response.json()[u'available']):
            raise BackendException((
                u'Out of space: trying to store "%s" (%d bytes), but only '
                u'%d bytes available on OneDrive.' % (
                    source_path.name, source_size,
                    response.json()[u'available'])))
        log.Debug(u"Checked quota in %fs" % (time.time() - start))

        with source_path.open() as source_file:
            start = time.time()
            # Create a BITS session, so that we can upload large files.
            short_directory_id = self.directory_id.split(u'.')[-1]
            url = u'https://cid-%s.users.storage.live.com/items/%s/%s' % (
                self.user_id, short_directory_id, remote_filename)
            headers = {
                u'X-Http-Method-Override': u'BITS_POST',
                u'BITS-Packet-Type': u'Create-Session',
                u'BITS-Supported-Protocols': self.BITS_1_5_UPLOAD_PROTOCOL,
            }

            response = self.http_client.post(
                url,
                headers=headers)
            response.raise_for_status()
            if (u'bits-packet-type' not in response.headers or
                    response.headers[u'bits-packet-type'].lower() != u'ack'):
                raise BackendException((
                    u'File "%s" cannot be uploaded: '
                    u'Could not create BITS session: '
                    u'Server response did not include BITS-Packet-Type: ACK' % (
                        remote_filename)))
            bits_session_id = response.headers[u'bits-session-id']
            log.Debug(u'BITS session id is "%s"' % bits_session_id)

            # Send fragments (with a maximum size of 60 MB each).
            offset = 0
            while True:
                chunk = source_file.read(self.MAXIMUM_FRAGMENT_SIZE)
                if len(chunk) == 0:
                    break
                headers = {
                    u'X-Http-Method-Override': u'BITS_POST',
                    u'BITS-Packet-Type': u'Fragment',
                    u'BITS-Session-Id': bits_session_id,
                    u'Content-Range': u'bytes %d-%d/%d' % (offset, offset + len(chunk) - 1, source_size),
                }
                response = self.http_client.post(
                    url,
                    headers=headers,
                    data=chunk)
                response.raise_for_status()
                offset += len(chunk)

            # Close the BITS session to commit the file.
            headers = {
                u'X-Http-Method-Override': u'BITS_POST',
                u'BITS-Packet-Type': u'Close-Session',
                u'BITS-Session-Id': bits_session_id,
            }
            response = self.http_client.post(url, headers=headers)
            response.raise_for_status()

            log.Debug(u"PUT file in %fs" % (time.time() - start))

    def _delete(self, remote_filename):
        file_id = self.get_file_id(remote_filename)
        if file_id is None:
            raise BackendException((
                u'File "%s" cannot be deleted: it does not exist' % (
                    remote_filename)))
        response = self.http_client.delete(self.API_URI + file_id)
        response.raise_for_status()

    def _query(self, remote_filename):
        file_id = self.get_file_id(remote_filename)
        if file_id is None:
            return {u'size': -1}
        response = self.http_client.get(self.API_URI + file_id)
        response.raise_for_status()
        if u'size' not in response.json():
            raise BackendException((
                u'Malformed JSON: expected "size" member in %s' % (
                    response.json())))
        return {u'size': response.json()[u'size']}

    def _retry_cleanup(self):
        self.initialize_oauth2_session()


duplicity.backend.register_backend(u'onedrive', OneDriveBackend)
