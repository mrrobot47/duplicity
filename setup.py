#!/usr/bin/env python3
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
from setuptools import setup, Extension
from setuptools.command.test import test
from setuptools.command.install import install
from setuptools.command.sdist import sdist
from distutils.command.build_scripts import build_scripts

version_string = u"$version"

if not (sys.version_info[:2] >= (3, 5) or (sys.version_info[0] == 2 and sys.version_info[:2] >= (2, 7))):
    print(u"Sorry, duplicity requires version 2.7 or version 3.5 or later of Python.")
    sys.exit(1)

incdir_list = libdir_list = None

if os.name == u'posix':
    LIBRSYNC_DIR = os.environ.get(u'LIBRSYNC_DIR', u'')
    args = sys.argv[:]
    for arg in args:
        if arg.startswith(u'--librsync-dir='):
            LIBRSYNC_DIR = arg.split(u'=')[1]
            sys.argv.remove(arg)
    if LIBRSYNC_DIR:
        incdir_list = [os.path.join(LIBRSYNC_DIR, u'include')]
        libdir_list = [os.path.join(LIBRSYNC_DIR, u'lib')]

data_files = [(u'share/man/man1',
               [u'bin/duplicity.1',
                u'bin/rdiffdir.1']),
              (u'share/doc/duplicity-%s' % version_string,
               [u'COPYING',
                u'README',
                u'README-REPO',
                u'README-LOG',
                u'CHANGELOG']),
              ]

top_dir = os.path.dirname(os.path.abspath(__file__))
assert os.path.exists(os.path.join(top_dir, u"po")), u"Missing 'po' directory."
for root, dirs, files in os.walk(os.path.join(top_dir, u"po")):
    for file in files:
        path = os.path.join(root, file)
        if path.endswith(u"duplicity.mo"):
            lang = os.path.split(root)[-1]
            data_files.append(
                (u'share/locale/%s/LC_MESSAGES' % lang,
                 [u"po/%s/duplicity.mo" % lang]))

if not os.environ.get(u'READTHEDOCS') == u'True':
    ext_modules=[Extension(name=r"duplicity._librsync",
                           sources=[r"duplicity/_librsyncmodule.c"],
                           include_dirs=incdir_list,
                           library_dirs=libdir_list,
                           libraries=[u"rsync"])]
else:
    ext_modules = []


class TestCommand(test):

    def run(self):
        # Make sure all modules are ready
        build_cmd = self.get_finalized_command(u"build_py")
        build_cmd.run()
        # And make sure our scripts are ready
        build_scripts_cmd = self.get_finalized_command(u"build_scripts")
        build_scripts_cmd.run()

        # make symlinks for test data
        if build_cmd.build_lib != top_dir:
            for path in [u'testfiles.tar.gz', u'gnupg']:
                src = os.path.join(top_dir, u'testing', path)
                target = os.path.join(build_cmd.build_lib, u'testing', path)
                try:
                    os.symlink(src, target)
                except Exception:
                    pass

        os.environ[u'PATH'] = u"%s:%s" % (
            os.path.abspath(build_scripts_cmd.build_dir),
            os.environ.get(u'PATH'))

        test.run(self)


class InstallCommand(install):

    def run(self):
        # Normally, install will call build().  But we want to delete the
        # testing dir between building and installing.  So we manually build
        # and mark ourselves to skip building when we run() for real.
        self.run_command(u'build')
        self.skip_build = True

        # This should always be true, but just to make sure!
        if self.build_lib != top_dir:
            testing_dir = os.path.join(self.build_lib, u'testing')
            os.system(u"rm -rf %s" % testing_dir)

        install.run(self)


# TODO: move logic from dist/makedist inline
class SDistCommand(sdist):

    def run(self):
        version = version_string
        if version[0] == u'$':
            version = u"0.0dev"
        os.system(os.path.join(top_dir, u"dist", u"makedist") + u" " + version)
        os.system(u"mkdir -p " + self.dist_dir)
        os.system(u"mv duplicity-" + version + u".tar.gz " + self.dist_dir)


# don't touch my shebang
class BSCommand (build_scripts):

    def run(self):
        u"""
        Copy, chmod each script listed in 'self.scripts'
        essentially this is the stripped
         distutils.command.build_scripts.copy_scripts()
        routine
        """
        from stat import ST_MODE
        from distutils.dep_util import newer
        from distutils import log

        self.mkpath(self.build_dir)
        outfiles = []
        for script in self.scripts:
            outfile = os.path.join(self.build_dir, os.path.basename(script))
            outfiles.append(outfile)

            if not self.force and not newer(script, outfile):
                log.debug(u"not copying %s (up-to-date)", script)
                continue

            log.info(u"copying and NOT adjusting %s -> %s", script,
                     self.build_dir)
            self.copy_file(script, outfile)

        if os.name == u'posix':
            for file in outfiles:
                if self.dry_run:
                    log.info(u"changing mode of %s", file)
                else:
                    oldmode = os.stat(file)[ST_MODE] & 0o7777
                    newmode = (oldmode | 0o555) & 0o7777
                    if newmode != oldmode:
                        log.info(u"changing mode of %s from %o to %o",
                                 file, oldmode, newmode)
                        os.chmod(file, newmode)


setup(name=u"duplicity",
    version=version_string,
    description=u"Encrypted backup using rsync algorithm",
    author=u"Ben Escoto <requested no contact>",
    author_email=u"<requested no contact>",
    maintainer=u"Kenneth Loafman <kenneth@loafman.com>",
    maintainer_email=u"kenneth@loafman.com",
    url=u"http://duplicity.nongnu.org/index.html",
    packages=[u'duplicity',
              u'duplicity.backends',
              u'duplicity.backends.pyrax_identity',
              u'testing',
              u'testing.functional',
              u'testing.overrides',
              u'testing.unit'],
    package_dir={u"duplicity": u"duplicity",
                 u"duplicity.backends": u"duplicity/backends", },
    ext_modules=ext_modules,
    scripts=[u'bin/rdiffdir', u'bin/duplicity'],
    data_files=data_files,
    setup_requires=[u'pytest-runner'],
    install_requires=[u'fasteners', u'future', 'python-gettext'],
    tests_require=[u'pytest',u'fasteners', u'future', u'mock', u'pexpect', 'python-gettext'],
    test_suite=u'testing',
    cmdclass={u'test': TestCommand,
              u'install': InstallCommand,
              u'sdist': SDistCommand,
              u'build_scripts': BSCommand},
    classifiers=[u"Programming Language :: Python :: 2",
                 u"Programming Language :: Python :: 2.7",
                 u"Programming Language :: Python :: 3",
                 u"Programming Language :: Python :: 3.5"]
    )
