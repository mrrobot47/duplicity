# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4; encoding:utf8 -*-
#
# Copyright 2014 Michael Terry <mike@mterry.name>
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

# This is just a small override to the system gettext.py which allows us to
# always return a string with fancy unicode characters, which will notify us
# if we ever get a unicode->ascii translation by accident.


def install(*args, **kwargs):  # pylint: disable=unused-argument
    ZWSP = u"​"  # ZERO WIDTH SPACE, basically an invisible space separator
    import sys
    if sys.version_info.major >= 3:
        import builtins
        b = builtins
    else:
        import __builtin__  # pylint: disable=import-error
        b = __builtin__
    b.__dict__[u'_'] = lambda x: x + ZWSP
    b.__dict__[u'ngettext'] = lambda one, more, n: one + ZWSP if n == 1 else more + ZWSP
