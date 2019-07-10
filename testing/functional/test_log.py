# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright 2008 Michael Terry <mike@mterry.name>
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

from __future__ import print_function
from future import standard_library
standard_library.install_aliases()

import unittest
import os

from . import FunctionalTestCase


class LogTest(FunctionalTestCase):
    u"""Test machine-readable functions/classes in log.py"""

    def setUp(self):
        super(LogTest, self).setUp()
        assert not os.system(u"rm -f /tmp/duplicity.log")

    def tearDown(self):
        super(LogTest, self).tearDown()
        assert not os.system(u"rm -f /tmp/duplicity.log")

    def test_command_line_error(self):
        u"""Check notification of a simple error code"""

        # Run actual duplicity command (will fail, because no arguments passed)
        basepython = os.environ.get(u'TOXPYTHON', None)
        if basepython is not None:
            os.system(u"%s ../bin/duplicity --log-file=/tmp/duplicity.log >/dev/null 2>&1" % (basepython,))
        else:
            os.system(u"../bin/duplicity --log-file=/tmp/duplicity.log >/dev/null 2>&1")

        # The format of the file should be:
        # """ERROR 2
        # . Blah blah blah.
        # . Blah blah blah.
        #
        # """
        f = open(u'/tmp/duplicity.log', u'r')
        linecount = 0
        lastline = False
        for line in f:
            assert(not lastline)
            linecount += 1
            if linecount == 1:
                assert(line == u"ERROR 2\n")
            elif line != u"\n":
                assert(line.startswith(r". "))
            else:
                lastline = True
        assert(lastline)


if __name__ == u"__main__":
    unittest.main()
