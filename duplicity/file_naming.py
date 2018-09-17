# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2002 Ben Escoto <ben@emerose.org>
# Copyright 2007 Kenneth Loafman <kenneth@loafman.com>
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

u"""Produce and parse the names of duplicity's backup files"""

import re
from duplicity import dup_time
from duplicity import globals

full_vol_re = None
full_vol_re_short = None
full_manifest_re = None
full_manifest_re_short = None
inc_vol_re = None
inc_vol_re_short = None
inc_manifest_re = None
inc_manifest_re_short = None
full_sig_re = None
full_sig_re_short = None
new_sig_re = None
new_sig_re_short = None


def prepare_regex(force=False):
    global full_vol_re
    global full_vol_re_short
    global full_manifest_re
    global full_manifest_re_short
    global inc_vol_re
    global inc_vol_re_short
    global inc_manifest_re
    global inc_manifest_re_short
    global full_sig_re
    global full_sig_re_short
    global new_sig_re
    global new_sig_re_short

    # we force regex re-generation in unit tests because file prefixes might have changed
    if full_vol_re and not force:
        return

    full_vol_re = re.compile(u"^" + globals.file_prefix + globals.file_prefix_archive + u"duplicity-full"
                             u"\\.(?P<time>.*?)"
                             u"\\.vol(?P<num>[0-9]+)"
                             u"\\.difftar"
                             u"(?P<partial>(\\.part))?"
                             u"($|\\.)")

    full_vol_re_short = re.compile(u"^" + globals.file_prefix + globals.file_prefix_archive + u"df"
                                   u"\\.(?P<time>[0-9a-z]+?)"
                                   u"\\.(?P<num>[0-9a-z]+)"
                                   u"\\.dt"
                                   u"(?P<partial>(\\.p))?"
                                   u"($|\\.)")

    full_manifest_re = re.compile(u"^" + globals.file_prefix + globals.file_prefix_manifest + u"duplicity-full"
                                  u"\\.(?P<time>.*?)"
                                  u"\\.manifest"
                                  u"(?P<partial>(\\.part))?"
                                  u"($|\\.)")

    full_manifest_re_short = re.compile(u"^" + globals.file_prefix + globals.file_prefix_manifest + u"df"
                                        u"\\.(?P<time>[0-9a-z]+?)"
                                        u"\\.m"
                                        u"(?P<partial>(\\.p))?"
                                        u"($|\\.)")

    inc_vol_re = re.compile(u"^" + globals.file_prefix + globals.file_prefix_archive + u"duplicity-inc"
                            u"\\.(?P<start_time>.*?)"
                            u"\\.to\\.(?P<end_time>.*?)"
                            u"\\.vol(?P<num>[0-9]+)"
                            u"\\.difftar"
                            u"($|\\.)")

    inc_vol_re_short = re.compile(u"^" + globals.file_prefix + globals.file_prefix_archive + u"di"
                                  u"\\.(?P<start_time>[0-9a-z]+?)"
                                  u"\\.(?P<end_time>[0-9a-z]+?)"
                                  u"\\.(?P<num>[0-9a-z]+)"
                                  u"\\.dt"
                                  u"($|\\.)")

    inc_manifest_re = re.compile(u"^" + globals.file_prefix + globals.file_prefix_manifest + u"duplicity-inc"
                                 u"\\.(?P<start_time>.*?)"
                                 u"\\.to"
                                 u"\\.(?P<end_time>.*?)"
                                 u"\\.manifest"
                                 u"(?P<partial>(\\.part))?"
                                 u"(\\.|$)")

    inc_manifest_re_short = re.compile(u"^" + globals.file_prefix + globals.file_prefix_manifest + u"di"
                                       u"\\.(?P<start_time>[0-9a-z]+?)"
                                       u"\\.(?P<end_time>[0-9a-z]+?)"
                                       u"\\.m"
                                       u"(?P<partial>(\\.p))?"
                                       u"(\\.|$)")

    full_sig_re = re.compile(u"^" + globals.file_prefix + globals.file_prefix_signature + u"duplicity-full-signatures"
                             u"\\.(?P<time>.*?)"
                             u"\\.sigtar"
                             u"(?P<partial>(\\.part))?"
                             u"(\\.|$)")

    full_sig_re_short = re.compile(u"^" + globals.file_prefix + globals.file_prefix_signature + u"dfs"
                                   u"\\.(?P<time>[0-9a-z]+?)"
                                   u"\\.st"
                                   u"(?P<partial>(\\.p))?"
                                   u"(\\.|$)")

    new_sig_re = re.compile(u"^" + globals.file_prefix + globals.file_prefix_signature + u"duplicity-new-signatures"
                            u"\\.(?P<start_time>.*?)"
                            u"\\.to"
                            u"\\.(?P<end_time>.*?)"
                            u"\\.sigtar"
                            u"(?P<partial>(\\.part))?"
                            u"(\\.|$)")

    new_sig_re_short = re.compile(u"^" + globals.file_prefix + globals.file_prefix_signature + u"dns"
                                  u"\\.(?P<start_time>[0-9a-z]+?)"
                                  u"\\.(?P<end_time>[0-9a-z]+?)"
                                  u"\\.st"
                                  u"(?P<partial>(\\.p))?"
                                  u"(\\.|$)")


def to_base36(n):
    u"""
    Return string representation of n in base 36 (use 0-9 and a-z)
    """
    div, mod = divmod(n, 36)
    if mod <= 9:
        last_digit = str(mod)
    else:
        last_digit = chr(ord(u'a') + mod - 10)
    if n == mod:
        return last_digit
    else:
        return to_base36(div) + last_digit


def from_base36(s):
    u"""
    Convert string s in base 36 to long int
    """
    total = 0
    for i in range(len(s)):
        total *= 36
        digit_ord = ord(s[i])
        if ord(u'0') <= digit_ord <= ord(u'9'):
            total += digit_ord - ord(u'0')
        elif ord(u'a') <= digit_ord <= ord(u'z'):
            total += digit_ord - ord(u'a') + 10
        else:
            assert 0, u"Digit %s in %s not in proper range" % (s[i], s)
    return total


def get_suffix(encrypted, gzipped):
    u"""
    Return appropriate suffix depending on status of
    encryption, compression, and short_filenames.
    """
    if encrypted:
        gzipped = False
    if encrypted:
        if globals.short_filenames:
            suffix = u'.g'
        else:
            suffix = u".gpg"
    elif gzipped:
        if globals.short_filenames:
            suffix = u".z"
        else:
            suffix = u'.gz'
    else:
        suffix = u""
    return suffix


def get(type, volume_number=None, manifest=False,
        encrypted=False, gzipped=False, partial=False):
    u"""
    Return duplicity filename of specified type

    type can be "full", "inc", "full-sig", or "new-sig". volume_number
    can be given with the full and inc types.  If manifest is true the
    filename is of a full or inc manifest file.
    """
    assert dup_time.curtimestr
    if encrypted:
        gzipped = False
    suffix = get_suffix(encrypted, gzipped)
    part_string = u""
    if globals.short_filenames:
        if partial:
            part_string = u".p"
    else:
        if partial:
            part_string = u".part"

    if type == u"full-sig" or type == u"new-sig":
        assert not volume_number and not manifest
        assert not (volume_number and part_string)
        if type == u"full-sig":
            if globals.short_filenames:
                return (globals.file_prefix + globals.file_prefix_signature +
                        u"dfs.%s.st%s%s" %
                        (to_base36(dup_time.curtime), part_string, suffix))
            else:
                return (globals.file_prefix + globals.file_prefix_signature +
                        u"duplicity-full-signatures.%s.sigtar%s%s" %
                        (dup_time.curtimestr, part_string, suffix))
        elif type == u"new-sig":
            if globals.short_filenames:
                return (globals.file_prefix + globals.file_prefix_signature +
                        u"dns.%s.%s.st%s%s" %
                        (to_base36(dup_time.prevtime),
                         to_base36(dup_time.curtime),
                         part_string, suffix))
            else:
                return (globals.file_prefix + globals.file_prefix_signature +
                        u"duplicity-new-signatures.%s.to.%s.sigtar%s%s" %
                        (dup_time.prevtimestr, dup_time.curtimestr,
                         part_string, suffix))
    else:
        assert volume_number or manifest
        assert not (volume_number and manifest)

        prefix = globals.file_prefix

        if volume_number:
            if globals.short_filenames:
                vol_string = u"%s.dt" % to_base36(volume_number)
            else:
                vol_string = u"vol%d.difftar" % volume_number
            prefix += globals.file_prefix_archive
        else:
            if globals.short_filenames:
                vol_string = u"m"
            else:
                vol_string = u"manifest"
            prefix += globals.file_prefix_manifest

        if type == u"full":
            if globals.short_filenames:
                return (u"%sdf.%s.%s%s%s" % (prefix, to_base36(dup_time.curtime),
                                             vol_string, part_string, suffix))
            else:
                return (u"%sduplicity-full.%s.%s%s%s" % (prefix, dup_time.curtimestr,
                                                         vol_string, part_string, suffix))
        elif type == u"inc":
            if globals.short_filenames:
                return (u"%sdi.%s.%s.%s%s%s" % (prefix, to_base36(dup_time.prevtime),
                                                to_base36(dup_time.curtime),
                                                vol_string, part_string, suffix))
            else:
                return (u"%sduplicity-inc.%s.to.%s.%s%s%s" % (prefix, dup_time.prevtimestr,
                                                              dup_time.curtimestr,
                                                              vol_string, part_string, suffix))
        else:
            assert 0


def parse(filename):
    u"""
    Parse duplicity filename, return None or ParseResults object
    """
    def str2time(timestr, short):
        u"""
        Return time in seconds if string can be converted, None otherwise
        """
        if short:
            t = from_base36(timestr)
        else:
            try:
                t = dup_time.genstrtotime(timestr.upper())
            except dup_time.TimeException:
                return None
        return t

    def get_vol_num(s, short):
        u"""
        Return volume number from volume number string
        """
        if short:
            return from_base36(s)
        else:
            return int(s)

    def check_full():
        u"""
        Return ParseResults if file is from full backup, None otherwise
        """
        prepare_regex()
        short = True
        m1 = full_vol_re_short.search(filename)
        m2 = full_manifest_re_short.search(filename)
        if not m1 and not m2 and not globals.short_filenames:
            short = False
            m1 = full_vol_re.search(filename)
            m2 = full_manifest_re.search(filename)
        if m1 or m2:
            t = str2time((m1 or m2).group(u"time"), short)
            if t:
                if m1:
                    return ParseResults(u"full", time=t,
                                        volume_number=get_vol_num(m1.group(u"num"), short))
                else:
                    return ParseResults(u"full", time=t, manifest=True,
                                        partial=(m2.group(u"partial") is not None))
        return None

    def check_inc():
        u"""
        Return ParseResults if file is from inc backup, None otherwise
        """
        prepare_regex()
        short = True
        m1 = inc_vol_re_short.search(filename)
        m2 = inc_manifest_re_short.search(filename)
        if not m1 and not m2 and not globals.short_filenames:
            short = False
            m1 = inc_vol_re.search(filename)
            m2 = inc_manifest_re.search(filename)
        if m1 or m2:
            t1 = str2time((m1 or m2).group(u"start_time"), short)
            t2 = str2time((m1 or m2).group(u"end_time"), short)
            if t1 and t2:
                if m1:
                    return ParseResults(u"inc", start_time=t1,
                                        end_time=t2, volume_number=get_vol_num(m1.group(u"num"), short))
                else:
                    return ParseResults(u"inc", start_time=t1, end_time=t2, manifest=1,
                                        partial=(m2.group(u"partial") is not None))
        return None

    def check_sig():
        u"""
        Return ParseResults if file is a signature, None otherwise
        """
        prepare_regex()
        short = True
        m = full_sig_re_short.search(filename)
        if not m and not globals.short_filenames:
            short = False
            m = full_sig_re.search(filename)
        if m:
            t = str2time(m.group(u"time"), short)
            if t:
                return ParseResults(u"full-sig", time=t,
                                    partial=(m.group(u"partial") is not None))
            else:
                return None

        short = True
        m = new_sig_re_short.search(filename)
        if not m and not globals.short_filenames:
            short = False
            m = new_sig_re.search(filename)
        if m:
            t1 = str2time(m.group(u"start_time"), short)
            t2 = str2time(m.group(u"end_time"), short)
            if t1 and t2:
                return ParseResults(u"new-sig", start_time=t1, end_time=t2,
                                    partial=(m.group(u"partial") is not None))
        return None

    def set_encryption_or_compression(pr):
        u"""
        Set encryption and compression flags in ParseResults pr
        """
        if (filename.endswith(u'.z') or
                not globals.short_filenames and filename.endswith(u'gz')):
            pr.compressed = 1
        else:
            pr.compressed = None

        if (filename.endswith(u'.g') or
                not globals.short_filenames and filename.endswith(u'.gpg')):
            pr.encrypted = 1
        else:
            pr.encrypted = None

    pr = check_full()
    if not pr:
        pr = check_inc()
        if not pr:
            pr = check_sig()
            if not pr:
                return None
    set_encryption_or_compression(pr)
    return pr


class ParseResults:
    u"""
    Hold information taken from a duplicity filename
    """
    def __init__(self, type, manifest=None, volume_number=None,
                 time=None, start_time=None, end_time=None,
                 encrypted=None, compressed=None, partial=False):

        assert type in [u"full-sig", u"new-sig", u"inc", u"full"]

        self.type = type
        if type == u"inc" or type == u"full":
            assert manifest or volume_number
        if type == u"inc" or type == u"new-sig":
            assert start_time and end_time
        else:
            assert time

        self.manifest = manifest
        self.volume_number = volume_number
        self.time = time
        self.start_time, self.end_time = start_time, end_time

        self.compressed = compressed  # true if gzip compressed
        self.encrypted = encrypted  # true if gpg encrypted

        self.partial = partial

    def __eq__(self, other):
        return self.type == other.type and \
            self.manifest == other.manifest and \
            self.time == other.time and \
            self.start_time == other.start_time and \
            self.end_time == other.end_time and \
            self.partial == other.partial
