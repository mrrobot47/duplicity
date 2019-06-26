#!/usr/bin/env python2
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

import sys
import os

from distutils.core import setup, Extension  # pylint: disable=import-error,no-name-in-module

assert len(sys.argv) == 1
sys.argv.append(u"build")

setup(name=r"CModule",
      version=u"cvs",
      description=u"duplicity's C component",
      ext_modules=[Extension(name=r"_librsync",
                             sources=[r"_librsyncmodule.c"],
                             libraries=[u"rsync"])])

assert not os.system(u"mv `find build -name '_librsync*.so'` .")
assert not os.system(u"rm -rf build")
