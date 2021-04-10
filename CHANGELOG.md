## (unreleased)

### New

* Merge branch 'google-drive-v3' into 'master' [Kenneth Loafman]

### Changes

* Remove installs common between before\_script: and script: [Kenneth Loafman]

* Remove installs common between before\_script: and script: [Kenneth Loafman]

### Fix

* Util.uexec() will return u'' if no err msg in e.args. [Kenneth Loafman]

* Util.uexec() should check for e==None on entry. [Kenneth Loafman]

* Fix bug #1547458 - more consistent passphrase prompt. [Kenneth Loafman]

* Fixes bug #1454136 - SX backend issues. [Kenneth Loafman]

* Fixes bug 1918981 - option to skip trash on delete on mediafire. [Kenneth Loafman]

* Fix bug 1919017 - MultiBackend reports failure on file deletion. [Kenneth Loafman]

* Fixes #41 - par2+rsync (non-ssh) fails. [Kenneth Loafman]

### Other

* Merge branch 'boxbackend' into 'master' [Kenneth Loafman]

* Implement Box backend. [Jason Wu]

* Merge branch 'megav3' into 'master' [Kenneth Loafman]

* Implement megav3 backend to to cater for change in MEGACmd. [Jason Wu]

* Merge branch 'master' of git@gitlab.com:duplicity/duplicity.git. [Kenneth Loafman]

* Merge branch 'use-new-azure-python-packages' into 'master' [Kenneth Loafman]

* Fix documentation for azure backend. [Michael Kopp]

* Merge branch 'master' into 'master' [Kenneth Loafman]

* Fix typo. [Moses Miller]

* Merge branch 'master' into 'master' [Kenneth Loafman]

* Add IDrive backend. [SmilingM]

* Merge branch 'master' into 'master' [Kenneth Loafman]

* Progress bar improvements. [Moses Miller]

* Fix;usr:Fixes bug #1652953 - seek(0) on /dev/stdin crashes. [Kenneth Loafman]

* Add a new Google Drive backend (gdrive:) [Jindřich Makovička]

* Merge branch 'azurev12' into 'master' [Kenneth Loafman]

* Replaced original azure implementation. [Erwin Bovendeur]

* Fixed code smells. [Erwin Bovendeur]

* Azure v12 support. [Erwin Bovendeur]

* Revert "fix:pkg:Remove requirement for python3-pytest-runner.  Not used." [Kenneth Loafman]

* Merge branch 'feature/list-required-volumes-on-restore-dry-run' into 'master' [Kenneth Loafman]

* List required volumes when called with 'restore --dry-run' [Matthias Blankertz]

* Merge branch 'swrmr-master-patch-23969' into 'master' [Kenneth Loafman]

* Fix sorting of BackupSets by avoiding direct comparison. [Stefan Wehrmeyer]

* Merge branch 'master' of gitlab.com:duplicity/duplicity. [Kenneth Loafman]

* Merge branch 'master' into 'master' [Kenneth Loafman]

* Update mailing list link. [Chris Coutinho]

* Merge branch 'master' of gitlab.com:duplicity/duplicity. [Kenneth Loafman]

* Fixes #16 - Move from boto to boto3. [Kenneth Loafman]

* Py27 EOL 01/2020, py35 EOL 01/2021, remove tests. [Kenneth Loafman]

* Remove 2to3 from ub16 builds. [Kenneth Loafman]

* Move py35 back to ub16, try 2. [Kenneth Loafman]

* Move py35 back to ub16. [Kenneth Loafman]

* Move py27 tests to ub16 and py35 tests to ub18. [Kenneth Loafman]

* Fixes #16 - Move from boto to boto3. [Kenneth Loafman]

* Py27 EOL 01/2020, py35 EOL 01/2021, remove tests. [Kenneth Loafman]

* Move py27 tests to ub16 and py35 tests to ub18. [Kenneth Loafman]

* Fixes #33, remove quotes from identity filename option. [Kenneth Loafman]

* Fix to correctly build \_librsync.so. [Kenneth Loafman]

* Fix to add --inplace option to build\_ext. [Kenneth Loafman]

* Rename pylintrc to .pylintrc. [Kenneth Loafman]

* Merge branch 'fix-prefix-affinity-registration' into 'master' [Kenneth Loafman]

* Multibackend: fix indentation error that was preventing from registering more than one affinity prefix per backend. [KheOps]

* Move testfiles dir to a temp location. [Kenneth Loafman]

* Merge remote-tracking branch 'alpha/testfiles' [Kenneth Loafman]

* Update .gitlab-ci.yml to need code test to pass. [Kenneth Loafman]

* Remove basepython in code and coverage tests. [Kenneth Loafman]

* Add report.xml. [Kenneth Loafman]

* Bulk replace testfiles with /tmp/testfiles. [Kenneth Loafman]

* Skip unicode tests that fail on non-Linux systems like macOS. [Kenneth Loafman]


## rel.0.8.18 (2021-01-09)

### Other

* Merge branch 'onedrive-token' into 'master' [Kenneth Loafman]

* Onedrive: Support using an external client id / refresh token. [Michael Terry]

* Update .gitlab-ci.yml to need code test to pass. [Kenneth Loafman]

* Merge branch 'master' of git@gitlab.com:duplicity/duplicity.git. [Kenneth Loafman]

* Fix issue #26 Backend b2 backblaze fails with nameprefix restrictions. [Kenneth Loafman]

* Fix issue #29 Backend b2 backblaze fails with nameprefix restrictions. [Kenneth Loafman]

* Fix unadorned strings. [Kenneth Loafman]

* Merge branch 'Rufflewind-master-patch-11811' into 'master' [Kenneth Loafman]

* Report errors if B2 backend does exist but otherwise fails to import. [Phil Ruffwind]

* Add report.xml. [Kenneth Loafman]

* Remove basepython in code and coverage tests. [Kenneth Loafman]

* Fix pep8 warning. [Kenneth Loafman]

* Added option --log-timestamp to prepend timestamp to log entry. [Kenneth Loafman]

* Merge branch 'master' of gitlab.com:duplicity/duplicity. [Kenneth Loafman]

* Merge branch 'master' into 'master' [Kenneth Loafman]

* Improve. [Gwyn Ciesla]

* Improve patch for Python 3.10. [Gwyn Ciesla]

* Conditionalize for Python version. [Gwyn Ciesla]

* Patch for Python 3.10. [Gwyn Ciesla]


## rel.0.8.17 (2020-11-11)

### Other

* Fixup ignore\_regexps for optional text. [Kenneth Loafman]

* Fix issue #26 (again) - duplicity does not clean up par2 files. [Kenneth Loafman]

* Fix issue #26 - duplicity does not clean up par2 files. [Kenneth Loafman]

* Fix issue #25 - Multibackend not deleting files. [Kenneth Loafman]

* Adjust setup.py for changelog changes. [Kenneth Loafman]

* Delete previous manual changelogs. [Kenneth Loafman]

* Tools to make a CHANGELOG.md from git commits. [Kenneth Loafman]

* Merge branch 'exc-if-present-robust' into 'master' [Kenneth Loafman]

* Make exclude-if-present more robust. [Michael Terry]

* Merge branch 'no-umask' into 'master' [Kenneth Loafman]

* Drop default umask of 0077. [Michael Terry]

* Comment out RsyncBackendTest, again. [Kenneth Loafman]

* Fix some unadorned strings. [Kenneth Loafman]

* Fixed RsyncBackendTeest with proper URL. [Kenneth Loafman]

* Merge branch 'Yump-issue-23' into 'master' [Kenneth Loafman]

* Fix issue #23. [Yump]

* Rclonebackend now logs at the same logging level as duplicity. [Kenneth Loafman]

* Allow sign-build to fail on walk away.  Need passwordless option. [Kenneth Loafman]

* Merge branch 'fix-rename' into 'master' [Kenneth Loafman]

* Fix --rename typo. [Michael Terry]

* Move back to VM build, not remote.  Too many issues with remote. [Kenneth Loafman]

* Merge branch 'escape-quote' into 'master' [Kenneth Loafman]

* Escape single quotes in machine-readable log messages. [Michael Terry]

* Uncomment review-tools for snap. [Kenneth Loafman]

* Whoops, missing wildcard '*'. [Kenneth Loafman]

* Changes to allow remote build of snap on LP. [Kenneth Loafman]

* Changes to allow remote build of snap on LP. [Kenneth Loafman]

* Add a pylint disable-import-error flag. [Kenneth Loafman]

* Change urllib2 to urllib.request in parse\_digest\_challenge(). [Kenneth Loafman]

* Fix Python 3.9 test in .gitlab-ci.yaml. [Kenneth Loafman]

* Fix Python 3.9 test in .gitlab-ci.yaml. [Kenneth Loafman]

* Add Python 3.9 to .gitlab-ci.yaml. [Kenneth Loafman]

* Add Python 3.9 to the test suite.  It tests sucessfuly. [Kenneth Loafman]

* Fix bug #1893481 again for Python2.  Missed include. [Kenneth Loafman]

* Fix bug #1893481 Error when logging improperly encoded filenames. [Kenneth Loafman]


## rel.0.8.16 (2020-09-29)

### Other

* Merged in s3-unfreeze-all. [Kenneth Loafman]

* Merge branch 's3-unfreeze-all' into 'master' [Kenneth Loafman]

* Wait for Glacier batch unfreeze to finish. [Marco Herrn]

* Adorn string as unicode. [Marco Herrn]

* Utilize ThreadPoolExecutor for S3 glacier unfreeze. [Marco Herrn]

* Refine codestyle according to PEP-8. [Marco Herrn]

* Adorn strings as unicode. [Marco Herrn]

* S3 unfreeze all files at once. [Marco Herrn]

* Add boto3 to list of requirements. [Kenneth Loafman]

* Remove ancient CVS Id macro. [Kenneth Loafman]

* Merged in OutlawPlz:paramiko-progress. [Kenneth Loafman]

* Merge branch 'paramiko-progress' into 'master' [Kenneth Loafman]

* Fixes paramiko backend progress bar. [Matteo Palazzo]

* Merged in lazy init for Boto3 network connections. [Kenneth Loafman]

* Merge branch 'feature/lazy\_init\_boto3' into 'master' [Kenneth Loafman]

* Initial crack at lazy init for Boto3. [Carl Alexander Adams]

* Merge branch 'hostname' into 'master' [Kenneth Loafman]

* Record the hostname, not the fqdn, in manifest files. [Michael Terry]

* Merge branch 'listdir-contains' into 'master' [Kenneth Loafman]

* Avoid calling stat when checking for exclude-if-present files. [Michael Terry]

* Fix build control files after markdown conversion. [Kenneth Loafman]

* Recover some changes lost after using web-ide. [Kenneth Loafman]

* Paperwork. [Kenneth Loafman]

* Merge branch 's3-boto3-region-and-endpoint' into 'master' [Kenneth Loafman]

* Set default values for s3\_region\_name and s3\_endpoint\_url. [Marco Herrn]

* Allow setting s3 region and endpoint. [Marco Herrn]

* Update README-REPO.md. [Kenneth Loafman]

* Make code view consistent. [Kenneth Loafman]

* Update setup.py. [Kenneth Loafman]

* Update README.md. [Kenneth Loafman]

* Paperwork. [Kenneth Loafman]

* Revert "Merge branch 's3-boto3-region-and-endpoint' into 'master'" [Kenneth Loafman]

* Bump version for LP dev build. [Kenneth Loafman]


## rel.0.8.15 (2020-07-27)

### Other

* Always paperwork. [Kenneth Loafman]

* Merge branch 's3-boto3-region-and-endpoint' into 'master' [Kenneth Loafman]

* Allow setting s3 region and endpoint. [Marco Herrn]

* Merge branch 'pydrive-notfound' into 'master' [Kenneth Loafman]

* Fix missing FileNotUploadedError in pydrive backend. [Martin Sucha]

* Merge branch 'pydriveshared' into 'master' [Kenneth Loafman]

* Fixed indentation. [Joshua Chan]

* Added shared drive support to existing `pydrive` backend instead of a new backend. [Joshua Chan]

* PydriveShared backend is identical to Pydrive backend, except that it works on shared drives rather than personal drives. [Joshua Chan]

* Include the query when parsing the backend URL string, so users can use it to pass supplementary info to the backend. [Joshua Chan]

* Fix caps on X-Python-Version. [Kenneth Loafman]

* Fix issue #10 - ppa:duplicity-*-git fails to install on Focal Fossa. [Kenneth Loafman]

* Merge branch 'patch-2' into 'master' [Kenneth Loafman]

* Remove python-cloudfiles from suggestions. [Jairo Llopis]

* Merge branch 'patch-1' into 'master' [Kenneth Loafman]

* Update azure requirement. [Jairo Llopis]

* Fix bug #1211481 with merge from Raffaele Di Campli. [Kenneth Loafman]

* Merge branch 'master' into 'master' [Kenneth Loafman]

* Added `--do-not-restore-ownership` option. [Jacotsu]

* Fix bug #1887689 with patch from Matthew Barry. [Kenneth Loafman]

* Bump version for LP build. [Kenneth Loafman]

* Merge branch 'fix-glacier-check' into 'master' [Kenneth Loafman]

* Fix check for s3 glacier/deep. [Michael Terry]

* Change from push to upload. [Kenneth Loafman]

* Add specific version for six. [Kenneth Loafman]


## rel.0.8.14 (2020-07-04)

### Other

* Set deprecation version to 0.9.0 for short filenames. [Kenneth Loafman]

* Fixes for issue #7, par2backend produces badly encoded filenames. [Kenneth Loafman]

* Added a couple of fsdecode calls for issue #7. [Kenneth Loafman]

* Generalize exception for failed get\_version() on LaunchPad. [Kenneth Loafman]

* Ignore *.so files. [Kenneth Loafman]

* Update docs. [Kenneth Loafman]

* Catch up on paperwork. [Kenneth Loafman]

* Merge branch 'mikix/rename-fix' into 'master' [Kenneth Loafman]

* Fix --rename encoding. [Michael Terry]

* Merge remote-tracking branch 'team/fix-py27-testing' [Kenneth Loafman]

* Skip tests failing on py27 under 18.04 (timing error). [Kenneth Loafman]

* Fix code style issue. [Kenneth Loafman]

* Add PATHS\_FROM\_ECLIPSE\_TO\_PYTHON to environ whan starting pydevd. [Kenneth Loafman]

* Add *.pyc to .gitignore. [Kenneth Loafman]

* Replace compilec.py with 'setup.py build\_ext', del compilec.py. [Kenneth Loafman]

* Fix unadorned string. [Kenneth Loafman]

* Fix usage of TOXPYTHON and overrides/bin shebangs. [Kenneth Loafman]

* Use default 'before\_script' for py27. [Kenneth Loafman]

* Don't collect coverage unless needed. [Kenneth Loafman]

* Merge branch 'master' into 'master' [Kenneth Loafman]

* Support PyDrive2 library in the pydrive backend. [Jindrich Makovicka]

* Merge branch 'Tidy\_up\_gitlab\_CI\_doc' into 'master' [Kenneth Loafman]

* Tidy .gitlab-ci.yml, fix py3.5 test, add py2.7 test (allowed to fail) [Aaron Whitehouse]

* Merge branch 'fix-py27-CI' [Kenneth Loafman]

* Test code instead of py27 since py27 is tested elsewhere. [Kenneth Loafman]

* Fix RdiffdirTest to use TOXPYTHON as well. [Kenneth Loafman]

* Set TOXPYTHON before tests. [Kenneth Loafman]

* Put TOXPYTHON in passed environment. [Kenneth Loafman]

* More fixes for bug #1877885 - Catch quota overflow on Mega upload. [Kenneth Loafman]

* More fixes for bug #1877885 - Catch quota overflow on Mega upload. [Kenneth Loafman]

* Undo: Try forcing python version to match tox testing version. [Kenneth Loafman]

* Always upgrade pip. [Kenneth Loafman]

* Try forcing python version to match tox testing version. [Kenneth Loafman]

* Uncomment all tests. [Kenneth Loafman]

* Test just py27 for now. [Kenneth Loafman]

* Replace bzr with git. [Kenneth Loafman]

* Don't load repo version of future, let pip do it. [Kenneth Loafman]

* Hmmm, Gitlab yaml does not like continuation lines.  Fix it. [Kenneth Loafman]

* Fix typo. [Kenneth Loafman]

* Update to use pip as module and add py35 test. [Kenneth Loafman]

* Add py35 to CI tests. [Kenneth Loafman]

* More changes to support Xenial. [Kenneth Loafman]

* Fix typo. [Kenneth Loafman]

* Fix duplicity to run under Python 3.5. [Kenneth Loafman]

* Fix duplicity to run under Python 3.5. [Kenneth Loafman]

* Merge branch 'add\_gitlab\_testing' into 'master' [Kenneth Loafman]

* Update .gitlab-ci.yml to update pip before installing other pip packages (to try to fix more-itertools issue: https://github.com/pytest-dev/pytest/issues/4770 ) [Aaron Whitehouse]

* Don't include .git dir when building docker images. [Kenneth Loafman]

* Merge branch 'update\_pip\_before\_install' into 'master' [Kenneth Loafman]

* Upgrade pip before installing requirements with it. Fixes more-itertools error as newer versions of pip identify that the latest more-itertools are incompatible with python 2. [Aaron Whitehouse]

* Patched in a megav2backend.py to update to MEGAcmd tools. [Kenneth Loafman]

* Change log.Warning to log.Warn.  Whoops! [Kenneth Loafman]

* Fixed bug #1875937 - validate\_encryption\_settings() fails w/S3 glacier. [Kenneth Loafman]

* Restore commented our backend requirements. [Kenneth Loafman]

* Fixes for rclonebackend from Francesco Magno (original author) [Kenneth Loafman]

* Version man pages during setup.py install. [Kenneth Loafman]

* More fixes for Launchpad build limitations. [Kenneth Loafman]

* More fixes for Launchpad build limitations. [Kenneth Loafman]

* Move setuptools\_scm to setup\_requires. [Kenneth Loafman]

* Back off requirements for fallback\_version in setup.py. [Kenneth Loafman]

* Add some requirements for LP build. [Kenneth Loafman]

* Make sure we get six from pip to support dropbox. [Kenneth Loafman]

* Provide fallback\_version for Launchpad builder. [Kenneth Loafman]

* Remove python3-setuptools-scm from setup.py. [Kenneth Loafman]

* Add python3-setuptools-scm to debian/control. [Kenneth Loafman]

* Try variation with hyphen seperator. [Kenneth Loafman]

* Try python3\_setuptools\_scm (apt repo name).  Probably too old. [Kenneth Loafman]

* Add setuptools\_scm to install\_requires. [Kenneth Loafman]


## rel.0.8.13 (2020-05-05)

### Other

* Fixed release date. [Kenneth Loafman]

* Fixed bug #1876446 - WebDAV backend creates only tiny or 0 Byte files. [Kenneth Loafman]

* Fix to run with --dist-dir command. [Kenneth Loafman]

* Fixed bug #1876778 - byte/str issues in megabackend.py. [Kenneth Loafman]

* Fix to use 'setup.py develop' instead of sdist. [Kenneth Loafman]

* Fix to run with --dist-dir command. [Kenneth Loafman]

* Fixed bug #1875529 - Support hiding instead of deletin on B2. [Kenneth Loafman]

* Uncomment upload and sign. [Kenneth Loafman]

* Reworked versioning to be git tag based. [Kenneth Loafman]

* Migrate bzr to git. [Kenneth Loafman]

* Fixed bug #1872332 - NameError in ssh\_paramiko\_backend.py. [ken]

* Fix spelling error. [ken]

* Fixed bug #1869921 - B2 backup resume fails for TypeError. [ken]

* Merged in lp:\~kenneth-loafman/duplicity/duplicity-pylint   - Enable additional pylint warnings. Make 1st pass at correction.       unused-argument,       unused-wildcard-import,       redefined-builtin,       bad-indentation,       mixed-indentation,      unreachable   - Renamed globals to config to fix conflict with \_\_builtin\_\_.glogals()   - Resolved conflict between duplicity.config and testing.manual.config   - Normalized emacs mode line to have encoding:utf8 on all *.py files. [ken]

* More changes for pylint. * Resolved conflict between duplicity.config and testing.manual.config * Normalized emacs mode line to have encoding:utf8 on all *.py files. [Kenneth Loafman]

* More changes for pylint. * Remove copy.com refs. [Kenneth Loafman]

* More changes for pylint. [Kenneth Loafman]

* More changes for pylint. [Kenneth Loafman]

* Enable additional pylint warnings.  Make 1st pass at correction.   - unused-argument,     unused-wildcard-import,     redefined-builtin,     bad-indentation,     mixed-indentation. [Kenneth Loafman]

* Fixed bug #1868414 - timeout parameter not passed to   BlobService for Azure backend. [Kenneth Loafman]


## rel.0.8.12 (2020-03-19)

### Other

* Merged in translation updates * Prep for 0.8.12. [Kenneth Loafman]

* Fixed bug #1867742 - TypeError: fsdecode()   takes 1 positional argument but 2 were given   with PCA backend. [Kenneth Loafman]

* Fixed bug #1867529 - UnicodeDecodeError: 'ascii'   codec can't decode byte 0x85 in position 0:   ordinal not in range(128) with PCA. [Kenneth Loafman]

* Fixed bug #1867468 - UnboundLocalError (local   variable 'ch\_err' referenced before assignment)   in ssh\_paramiko\_backend.py. [Kenneth Loafman]

* Fixed bug #1867444 - UnicodeDecodeError: 'ascii'   codec can't decode byte 0x85 in position 0:   ordinal not in range(128) using PCA backend. [Kenneth Loafman]

* Fixed bug #1867435 - TypeError: must be str,   not bytes using PCA backend. [Kenneth Loafman]

* Move pylint config from test\_code to pylintrc. [Kenneth Loafman]

* Cleaned up some setup issues where the man pages   and snapcraft.yaml were not getting versioned. [Kenneth Loafman]

* Fixed bug #1769267 - [enhancement] please consider   using rclone as backend. [Kenneth Loafman]

* Fixed bug #1755955 - best order is unclear,   of exclude-if-present and exclude-device-files   - Removed warning and will now allow these two to     be in any order.  If encountered outside of the     first two slots, duplicity will silently move     them to be in the first two slots.  Within those     two slots the order does not matter. [ken]

* Fixed a couple of file history bugs:   - #1044715 Provide a file history feature     + removed neutering done between series   - #1526557 --file-changed does not work     + fixed str/bytes issue finding filename. [ken]

* Fixed bug #1865648 - module 'multiprocessing.dummy' has   no attribute 'cpu\_count'.   - replaced with module psutil for cpu\_count() only   - appears Arch Linux does not support multiprocessing. [ken]

* Mod to get focal build on LP working. [ken]

* Mod to get focal build on LP working. [ken]

* Mod to get focal build on LP working. [ken]


## rel.0.8.11 (2020-02-24)

### Other

* Merged in translation updates. [ken]

* Fixed to work around par2 0.8.1 core dump on short name   - https://github.com/Parchive/par2cmdline/issues/145. [ken]

* Fixed bug #1857818 - startswith first arg must be bytes   - use util.fsdecode on filename. [ken]

* Fixed bug #1863018 - mediafire backend fails on py3   - Fixed handling of bytes filename in url. [ken]

* Add rclone requirement to snapcraft.yaml. [ken]

* Fixed bug #1236248 - --extra-clean clobbers old backups   - Removed --extra-clean, code, and docs. [ken]

* Fixed bug #1862672 - test\_log does not respect TMPDIR   - Patch supplied by Jan Tojnar. [ken]

* Fixed bug #1860405 - Auth mechanism not supported   - Added python3-boto3 requirement to snapcraft.yaml. [ken]

* More readthedocs munges. [ken]

* Don't format the po files for readthedocs. [ken]

* Add readthedocs.yaml config file, try 3. [ken]

* Add readthedocs.yaml config file, try 2. [ken]

* Add readthedocs.yaml config file. [ken]

* Remove intltool for readthedocs builder. [ken]

* Add python-gettext for readthedocs builder. [ken]

* Add gettext/intltool for readthedocs builder. [ken]

* Add gettext for readthedocs builder. [ken]

* Add intltool for readthedocs builder. [ken]

* Add intltools for readthedocs builder. [ken]

* Add intltools for readthedocs builder. [ken]

* Point readthedocs.io to this repo. [ken]

* Renamed botobackend.py to s3\_boto\_backend.py. [ken]

* Renamed botobackend.py to s3\_boto\_backend.py. [ken]

* Merged from parent to bring in changes. [Byron Hammond]

* Renamed MulitGzipFile to GzipFile to avoid future problems with upstream author of mgzip fixing the Mulit -> Multi typo. [Byron Hammond]

* Adding missed mgzip import and adjusting untouched unit tests. [Byron Hammond]

* Adding multi-core support by using mgzip instead of gzip. [Byron Hammond]

* Missing comma. [ken]

* Some code cleanup and play with docs. [ken]

* Uncomment snapcraft sign-build.  Seems it's fixed now. [ken]

* Fix argument order on review-tools. [ken]

* Reworked setup.py to build a pip-compatible   distribution tarball of duplicity. * Added dist/makepip for convenience. [ken]

* Adjust Dockerfiles to new requirements. [ken]

* Fix bug #1861287 - Removing old backup chains   fails using pexpect+sftp. [ken]

* Adjust Dockerfiles to new requirements. [ken]

* Enhance setup.py/cfg to allow install by pip. [ken]

* Enhance setup.py/cfg to allow install by pip. [ken]

* Enhance setup.py/cfg to allow install by pip. [ken]

* Bump version. [Kenneth Loafman]

* Gave up fighting the fascist version control   munging on snapcraft.io.  Duplicity now has the   form 0.8.10.1558, where the last number is the   bzr revno.  Can't do something nice like having   a dev/fin indicator like 0.8.10dev1558 for dev   versions and a fin for release or final. [Kenneth Loafman]


## rel.0.8.10 (2020-01-23)

### Other

* Merged in translation updates * Prep for 0.8.10. [Kenneth Loafman]

* Fixed bug #1858207 missing targets in multibackend   - Made it possible to return default value instead     of taking a fatal exception on an operation by     operation approach.  The only use case now is for     multibackend to be able to list all targets and     report back on the ones that don't work. [Kenneth Loafman]

* Fixed bug #1858204 - ENODEV should be added to   list of recognized error stringa. [Kenneth Loafman]

* Comment out test\_compare, again. [Kenneth Loafman]

* Clean up deprecation errors in Python 3.8. [Kenneth Loafman]

* Clean up some TODO tasks in testing code. [kenneth@loafman.com]

* Skip functional/test\_selection::TestUnicode if   python version is less than 3.7. [kenneth@loafman.com]

* Fixed bug #1859877 - syntax warning on python 3.8. [kenneth@loafman.com]

* Move to single-sourceing the package version   - Rework setup.py, dist/makedist, dist/makesnap,     etc., to get version from duplicity/\_\_init\_\_.py   - Drop dist/relfiles.  It was problematic. [kenneth@loafman.com]

* Fixed bug #1859304 with patch from Arduous   - Backup and restore do not work on SCP backend. [kenneth@loafman.com]

* Revert last change to duplicity.\_\_init\_\_.py. [kenneth@loafman.com]

* Py27 supports unicode returns for translations   - remove install that does not incude unicode   - Removed some unneeded includes of gettext. [kenneth@loafman.com]

* Fixed bug #1858713 - paramiko socket.timeout   - chan.recv() can return bytes or str based on     the phase of the moon.  Make allowances. [kenneth@loafman.com]

* Switched to python3 for snaps. [kenneth@loafman.com]

* Fix unadorned string. [kenneth@loafman.com]


## rel.0.8.09 (2020-01-07)

### Other

* Merged in translation updates * Prep for 0.8.09. [kenneth@loafman.com]

* Change of plans.  Skip test if rclone not present. [kenneth@loafman.com]

* Add rclone to setup testing requirements. [kenneth@loafman.com]

* Revert to testing after build. [kenneth@loafman.com]

* Fixed bug #1855736 again - Duplicity fails to start   - remove decode from unicode string. [kenneth@loafman.com]

* Fixed bug #1858295 - Unicode error in source filename   - decode arg if it comes in as bytes. [kenneth@loafman.com]

* Add snapcraft login to makesnap. [kenneth@loafman.com]

* Fix bug #1858153 with patch from az   - mega backend: fails to create directory. [kenneth@loafman.com]

* Fix bug #1857734 - TypeError in ssh\_paramiko\_backend   - conn.recv() can return bytes or string, make string. [kenneth@loafman.com]

* Fix bytes/string differences in subprocess\_popen()   - Now returns unicode string not bytes, like python2. [kenneth@loafman.com]

* Convert all shebangs to python3 for bug #1855736. [kenneth@loafman.com]

* Fixed bug #1857554 name 'file' is not defined   - file() calls replaced by open() in 3 places. [kenneth@loafman.com]

* Original rclonebackend.py from Francesco Magno for Python 2.7. [kenneth@loafman.com]

* Merged in lp:\~ed.so/duplicity/boto.fixup   - fix manpage indention   - clarify difference between boto backends   - add boto+s3:// for future use when boto3+s3://     will become default s3 backend. [kenneth@loafman.com]

* Fix manpage indention clarify difference between boto backends add boto+s3:// for future use when boto3+s3:// will become default s3 backend. [ed.so]

* Renamed testing/infrastructure to testing/docker. [kenneth@loafman.com]

* Fixed a mess I made.  setup.py was shebanged to   Py3, duplicity was shebanged to Py2.  This meant   that duplicity ran as Py2 but could not find its   modules because they were under Py3.  AArgh! [kenneth@loafman.com]

* Fixed bug #1855736 - duplicity fails to start   - Made imports absolute in dup\_main.py. [kenneth@loafman.com]

* Fixed bug #1856447 with hint from Enno L   - Replaced with formatted string. [kenneth@loafman.com]

* Fixed bug #1855736 with help from Michael Terry   - Decode Popen output to utf8. [kenneth@loafman.com]

* Fixed bug #1855636 with patch from Filip Slunecko   - Wrong buf type returned on error.  Make bytes. [kenneth@loafman.com]


## rel.0.8.08 (2019-12-08)

### Other

* Merged in translation updates. [kenneth@loafman.com]

* Merged in translation updates. [kenneth@loafman.com]

* Removed abandoned ref in README * Comment out signing in makesnap. [kenneth@loafman.com]

* Fixed bug #1854554 with help from Tommy Nguyen   - Fixed a typo made during Python 3 conversion. [kenneth@loafman.com]

* Fixed bug #1855379 with patch from Daniel González Gasull   - Issue warning on temporary connection loss. * Fixed misc coding style errors. [kenneth@loafman.com]

* Disabling autotest for LP build.  I have run tests on all Ubuntu releases since 18.04, so the code works.  To run tests manually, run tox from the main directory.  Maybe LP build will work again soon. [kenneth@loafman.com]

* Merged in lp:\~carlalex/duplicity/duplicity   - Fixes bug #1840044: Migrate boto backend to boto3   - New module uses boto3+s3:// as schema. [kenneth@loafman.com]

* Update to manpage. [Carl A. Adams]

* BUGFIX: list should retun byte strings, not unicode strings. [Carl A. Adams]

* Updating comments. [Carl A. Adams]

* Select boto3/s3 backend via url scheme rather than by CLI option.  Doc changes to support this. [Carl A. Adams]

* Renaming boto3 backend file. [Carl A. Adams]

* Merging from parent. [Carl A. Adams]

* Adding support for AWS Glacier Deep Archive.  Fixing some typos. [Carl A. Adams]

* Manpage updates.  Cleaning up the comments to reflect my current plans. Some minor clean-ups. [Carl A. Adams]

* Updating comments. [Carl A. Adams]

* SSE options comitted. AES tested, KMS not tested. [Carl A. Adams]

* Handling storage class on backup. [Carl A. Adams]

* Handling storage class on backup. [Carl A. Adams]

* Minor clean-ups. [Carl A. Adams]

* Rename boto3 backend py file. [Carl A. Adams]

* Removing 'todo' comment for multi support.  Defaults in Boto3 chunk the upload and attempt to use multiple threads.  See https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/s3.html#boto3.s3.transfer.TransferConfig. [Carl A. Adams]

* Format fix. [Carl A. Adams]

* Fixing status reporting.  Cleanup. [Carl A. Adams]

* Better exception handling. Return -1 for unknwon objects in \_query. [Carl A. Adams]

* Updating comment. [Carl A. Adams]

* Making note of a bug. [Carl A. Adams]

* Removing unused imports. [Carl A. Adams]

* Implementing \_query for boto3. [Carl A. Adams]

* Minor clean-up. [Carl A. Adams]

* Some initial work on a boto3 back end. [Carl A. Adams]

* Convert debian build to Python 3. [kenneth@loafman.com]

* Replace python with python3 in shebang. [kenneth@loafman.com]

* Convert debian build to Python 3. [kenneth@loafman.com]

* Fixed bug #1853809 - Tests failing with Python 3.8 / Deprecation warnings   - Fixed the deprecation warnings with patch from Sebastien Bacher   - Fixed test\_globmatch to handle python 3.8 same as 3.7   - Fixed tox.ini to include python 3.8 in future tests. [kenneth@loafman.com]

* Fixed bug #1853655 - duplicity crashes with --exclude-older-than   - The exclusion setup checked for valid string only.  Made     the code comprehend datetime (int) as well. [kenneth@loafman.com]

* Just some cosmetic changes. [kenneth@loafman.com]

* Fixed bug #1851668 with help from Wolfgang Rohdewald   - Applied patches to handle translations. [kenneth@loafman.com]

* Fixed bug #1852876 '\_io.BufferedReader' object has no attribute 'uc\_name'   - Fixed a couple of instances where str() was used in place of util.uexc()   - The file was opened with builtins, so use name, not uc\_name. [kenneth@loafman.com]

* Added build signing to dist/makesnap. [kenneth@loafman.com]

* Fixed bug #1852848 with patch from Tomas Krizek   - B2 moved the API from "b2" package into a separate "b2sdk" package.     Using the old "b2" package is now deprecated. See link:     https://github.com/Backblaze/B2\_Command\_Line\_Tool/blob/master/b2/\_sdk\_deprecation.py   - b2backend.py currently depends on both "b2" and "b2sdk", but use of "b2"     is enforced and "b2sdk" isn't used at all.   - The attached patch uses "b2sdk" as the primary dependency. If the new     "b2sdk" module isn't available, it falls back to using the old "b2" in     order to keep backward compatibility with older installations. [kenneth@loafman.com]


## rel.0.8.07 (2019-11-14)

### Other

* Merged in translation updates * Prep for 0.8.07. [kenneth@loafman.com]

* Fixed bug #1851727 - InvalidBackendURL for multi backend   - Encode to utf8 only on Python2, otherwise leave as unicode. [kenneth@loafman.com]

* Merged in lp:\~mterry/duplicity/resume-encrypt-no-pass   - This branch arose from a Debian patch that has been disabling the     encryption validation of volume1 during restarts for years.   - Debian has been preserving the ability to back up with just an encrypt     key and no password (i.e. to have no secrets on the backup machine). [kenneth@loafman.com]

* Fix resuming without a passphrase when using just an encryption key. [Michael Terry]

* Merged in lp:\~mterry/duplicity/pydrive-cache-fix   - The pydrive backend had another of the ongoing bytes/string issues. :)   - This time, it was saving a bytes filename in its internal cache after     each volume upload. Then when asked for a list of files later, it     would add the byte-filenames from its cache to the results.     And we'd end up thinking there were two of the same filename on the backend,     which would cause a crash at the end of an otherwise successful backup,     because the collections code would assert on the filenames being unique. [kenneth@loafman.com]

* Fix bytes/string issue in pydrive backend upload. [Michael Terry]

* Fixed bug #1851167 with help from Aspen Barnes   - Had Popen() to return strings not bytes. [kenneth@loafman.com]

* Added dist/makesnap to make spaps automagically. [kenneth@loafman.com]

* Fixed bug #1850990 with suggestion from Jon Wilson   - --s3-use-glacier and --no-encryption cause slow backups. [kenneth@loafman.com]

* Fix header in CHANGELOG. [kenneth@loafman.com]

* Added b2sdk to snapcraft.yaml * Fixed bug #1850440 - Can't mix strings and bytes. [kenneth@loafman.com]


## rel.0.8.06 (2019-11-05)

### Other

* Merged in translation updates. [kenneth@loafman.com]

* Updated snapcraft.yaml to remove python-lockfile and fix spelling. [kenneth@loafman.com]

* Updated snapcraft.yaml to remove rdiffdir and add libaft1 to stage. [kenneth@loafman.com]

* Updated snapcraft.yaml to include rdiffdir and did some reformatting. [kenneth@loafman.com]

* Updated snapcraft.yaml to include rdiffdir and did some reformatting. [kenneth@loafman.com]

* Removed file() call in swiftbackend.  It's been deprecated since py2. [kenneth@loafman.com]

* Revisited bug #1848783 - par2+webdav raises TypeError on Python 3   - Fixed so bytes filenames were compared as unicode in re.match() [kenneth@loafman.com]

* Removed a couple of disables from pylint code test.   - E1103 - Maybe has no member   - E0712 - Catching an exception which doesn't inherit from BaseException. [kenneth@loafman.com]

* Added additional fsdecode's to uses of local\_path.name and   source\_path.name in b2backend's \_get() and \_put.  See bug   #1847885 for more details. [kenneth@loafman.com]

* Fixed bug #1849661 with patch from Graham Cobb   - The problem is that b2backend uses 'quote\_plus' on the     destination URL without specifying the 'safe' argument as     '/'. Note that 'quote' defaults 'safe' to '/', but     'quote\_plus' does not! [kenneth@loafman.com]

* Fixed bug #1848166 - Swift backend fails on string concat   - added util.fsdecode() where needed. [kenneth@loafman.com]

* Fixed bug #1848783 with patch from Jacob Middag   - Don't use b'' strings in re.* [kenneth@loafman.com]

* Fixed bug #1848783 with patch from Jacob Middag   - Don't use b'' strings in re.* [kenneth@loafman.com]

* Fixed bug #1626061 with patch from Michael Apozyan   - While doing multipart upload to s3 we need to report the     total size of uploaded data, and not the size of each part     individually.  So we need to keep track of all parts     uploaded so far and sum it up on the fly. [kenneth@loafman.com]

* Removed revision 1480 until patch is validated. [kenneth@loafman.com]

* Fixed bug #1626061 with patch from Michael Apozyan   - While doing multipart upload to s3 we need to report the     total size of uploaded data, and not the size of each part     individually.  So we need to keep track of all parts     uploaded so far and sum it up on the fly. [kenneth@loafman.com]

* Fixed bug #1848203 with patch from Michael Apozyan   - convert to integer division. [kenneth@loafman.com]

* Fix unadorned string. [kenneth@loafman.com]

* Fix unadorned string. [kenneth@loafman.com]

* Updated b2 backend to work with both v0 and v1 of b2sdk * Fixed bug #1847885 - B2 fails on string concatenation.   - use util.fsdecode() to get a string not bytes.   - Partially fixed in bug #1843995, this applies same fix to     remaining instances of the problem. [kenneth@loafman.com]

* Update changelogs. [Adam Jacobs]

* In version 1 of the B2sdk, the list\_file\_names method is removed from the B2Bucket class. [Adam Jacobs]

* Complete fix for string concatenation in b2 backend. [Adam Jacobs]

* Fixed Resouce warnings when using paramiko.  It turns out   that duplicity's ssh\_paramiko\_backend.py was not handling   warning suppression and ended up clearing all warnings,   including those that default to off. [kenneth@loafman.com]

* Fixed Resouce warnings when using paramiko.  It turns out   that duplicity's ssh\_paramiko\_backend.py was not handling   warning suppression and ended up clearing all warnings,   including those that default to off. [kenneth@loafman.com]


## rel.0.8.05 (2019-10-07)

### Other

* Removed a setting in tox.ini that causes coverage to   be activated during testing duplicity. [kenneth@loafman.com]

* Merged in translation updates * Prep for 0.8.05. [kenneth@loafman.com]

* Fixed bug #1846678 - --exclude-device-files and -other-filesystems crashes   - assuming all options had arguments was fixed. [kenneth@loafman.com]

* Fixed bug #1844950 - ssh-pexpect backend syntax error   - put the global before the import. [kenneth@loafman.com]

* Fixed bug #1846167 - webdavbackend.py: expected bytes-like object, not str   - base64 now returns bytes where it used to be strings, so just decode(). [kenneth@loafman.com]

* Fixed bug reported on maillist - Python error in Webdav backend.  See:   https://lists.nongnu.org/archive/html/duplicity-talk/2019-09/msg00026.html. [kenneth@loafman.com]

* Fix bug #1844750 - RsyncBackend fails if used with multi-backend.   - used patch provided by KDM to fix. [kenneth@loafman.com]

* Fix bug #1843995 - B2 fails on string concatenation.   - use util.fsdecode() to get a string not bytes. [kenneth@loafman.com]

* Clean up some pylint warnings. [kenneth@loafman.com]

* Add testenv:coverage and took it out of defaults.  Some cleanup. [kenneth@loafman.com]

* Fix MacOS tempfile selection to avoid /tmp and /var/tmp.  See thread:   https://lists.nongnu.org/archive/html/duplicity-talk/2019-09/msg00000.html. [kenneth@loafman.com]

* Sort of fix bugs #1836887 and #1836888 by skipping the   tests under question when running on ppc64el machines. [kenneth@loafman.com]

* Added more python future includes to support using   python3 code mixed with python2. [kenneth@loafman.com]

* Fix exc.args handling.  Sometimes it's (message, int),   other times its (int, message).  We look for the   message and use that for the exception report. [kenneth@loafman.com]

* Adjust exclusion list for rsync into duplicity\_test. [kenneth@loafman.com]

* Set to allow pydevd usage during tox testing. [kenneth@loafman.com]

* Don't add extra newline when building dist/relfiles.txt. [kenneth@loafman.com]

* Changed dist/makedist to fall back to dist/relfiles.txt   in case bzr or git is not available to get files list.   Tox sdist needs setup.py which needs dist/makedist. * Updatated LINGUAS file to add four new translations. [kenneth@loafman.com]


## rel.0.8.04 (2019-08-31)

### Other

* Merged in translation updates * Prep for 0.8.04. [kenneth@loafman.com]

* Made some changes to the Docker infrastructure:   - All scripts run from any directory, assuming directory     structure remains the same.   - Changed from Docker's COPY internal command which is slow to     using external rsync which is faster and allows excludes.   - Removed a couple of unused files. [kenneth@loafman.com]

* Run compilec.py for code tests, it needs the import. [kenneth@loafman.com]

* Merged in lp:\~aaron-whitehouse/duplicity/08-docker-local-import   - Convert the Docker infrastructure to pull the local branch into     duplicity\_test. This allows testing the local branch with the     known-good Docker environment, even if it has not yet been     committed to trunk.   - As a consequence, remove the -r option to build-duplicity\_test.sh.     This functionality can be achieved by branching that revision     before running the script. [kenneth@loafman.com]

* Simplify README-TESTING and change this to recommend using the Docker images to test local branches in a known-good environment. [Aaron A Whitehouse]

* Convert Dockerfile-19.10 to new approach (using local folder instead of remote repo) * run-tests passes on 19.10 Docker (clean: commands succeeded; py27: commands succeeded; SKIPPED: py36: InterpreterNotFound: python3.6; py37: commands succeeded; report: commands succeeded) [Aaron A Whitehouse]

* Convert Dockerfile-19.04 to new approach (using local folder instead of remote repo) * run-tests passes on 19.04 Docker (clean: commands succeeded; py27: commands succeeded; SKIPPED:  py36: InterpreterNotFound: python3.6;  py37: commands succeeded; report: commands succeeded) [Aaron A Whitehouse]

* Edit Dockerfile-18.10 to use the local folder. * Tests all pass on 18.10 except for the same failures as trunk (4 failures on python 3.6: TestUnicode.test\_unicode\_filelist; TestUnicode.test\_unicode\_paths\_asterisks; TestUnicode.test\_unicode\_paths\_non\_globbing; TestUnicode.test\_unicode\_paths\_square\_brackets) [Aaron A Whitehouse]

* Use local folder instead of bzr revision, so remove the revision arguments in the setup script. * Modify Dockerfile and Dockerfile-18.04 to copy the local folder rather than the remote repository. * Tests all pass on 18.04 except for the same failures as trunk (4 failures on python 3.6: TestUnicode.test\_unicode\_filelist; TestUnicode.test\_unicode\_paths\_asterisks; TestUnicode.test\_unicode\_paths\_non\_globbing; TestUnicode.test\_unicode\_paths\_square\_brackets) [Aaron A Whitehouse]

* Merge with trunk. [Aaron A Whitehouse]

* Fix .bzrignore. [kenneth@loafman.com]

* Merged in lp:\~kaffeekiffer/duplicity/azure-filename   - Encode Azure back-end paths. [kenneth@loafman.com]

* Encode Azure backend file names. [Frank Fischer]

* Merged in lp:\~aaron-whitehouse/duplicity/08-README-TESTING   - Change README-TESTING to be correct for running individual tests     now that we have moved to Tox/Pytest. [kenneth@loafman.com]

* Change README-TESTING to be correct for running individual tests now that we have moved to Pytest. [Aaron A Whitehouse]

* Fix debian/rules file. [kenneth@loafman.com]

* Fix setup.py shebang. [kenneth@loafman.com]

* Fix debian/rules file. [kenneth@loafman.com]

* Fix debian/rules file. [kenneth@loafman.com]

* Fix debian/rules file. [kenneth@loafman.com]

* Fix debian/control file. [kenneth@loafman.com]

* Fix debian/control file. [kenneth@loafman.com]

* Fix debian/control file. [kenneth@loafman.com]

* Fix debian/control file. [kenneth@loafman.com]

* Fix debian/control file. [kenneth@loafman.com]

* Fix debian/control file. [kenneth@loafman.com]

* Fix debian/control file. [kenneth@loafman.com]

* Fix debian/control file. [kenneth@loafman.com]

* Fix debian/control file. [kenneth@loafman.com]

* Fix debian/control file. [kenneth@loafman.com]

* Ran futurize selectively filter-by-filter to find the ones that work. [kenneth@loafman.com]

* Fixed build on Launchpad for 0.8.x, so now there is a new PPA at   https://launchpad.net/\~duplicity-team/+archive/ubuntu/daily-dev-trunk. [kenneth@loafman.com]

* Fix debian/control file. [kenneth@loafman.com]

* Fix debian/control file. [kenneth@loafman.com]

* Merged in lp:\~aaron-whitehouse/duplicity/08-snap-python2   - Add packaging code for Snapcraft/Snap packages. [kenneth@loafman.com]

* Add snap package creation files * Modify dist/makedist to version the snapcraft.yaml. [Aaron A Whitehouse]

* Remove a mess I made. [Kenneth Loafman]

* Fixed bug #1839886 with hint from denick   - Duplicity crashes when using --file-prefix * Removed socket.settimeout from backend.py.   It was already set in commandline.py. * Removed pycryptopp from README requirements. [kenneth@loafman.com]

* Fixed bug #1839728 with info from Avleen Vig   - b2 backend requires additional import. [kenneth@loafman.com]

* Convert the docker duplicity\_test image to pull the local branch into the container, rather than lp:duplicity. This allows the use of the duplicity Docker testing containers to test local changes in a known-good environment before they are merged into trunk. The equivalent of the old behaviour can be achieved by starting with a clean branch from lp:duplicity. * Expand Docker context to parent branch folder and use -f in the docker build command to point to the Dockerfile. * Simplify build-duplicity\_test.sh now that the whole folder is copied (individual files no longer need to be copied) [Aaron A Whitehouse]


## rel.0.8.03 (2019-08-09)

### Other

* Merged in translation updates * Prep for 0.8.03. [kenneth@loafman.com]

* More changes to provide Python test coverage:   - Moved bulk of code from bin/duplicity to     duplicity/dup\_main.py for coverage. * Fixed some 2to3 issues in dup\_main.py * Fixed division differences with futurize. [kenneth@loafman.com]

* More changes to provide Python test coverage:   - Moved bulk of code from bin/duplicity to     duplicity/dup\_main.py for coverage. * Fixed some 2to3 issues in dup\_main.py * Fixed division differences with futurize. [kenneth@loafman.com]

* More changes to provide Python test coverage:   - Moved bulk of code from bin/duplicity to     duplicity/dup\_main.py for coverage. * Fixed some 2to3 issues in dup\_main.py. [kenneth@loafman.com]

* More changes to provide Python test coverage:   - Now covers functional tests spawning duplicity   - Does not cover bin/duplicity for some reason. [kenneth@loafman.com]

* Fixed bugs #1838427 and #1838702 with a fix   suggested by Stephen Miller.  The fix was to   supply tarfile with a unicode grpid, not bytes. [kenneth@loafman.com]

* Some changes to provide Python test coverage:   - Coverage runs with every test cycle   - Does not cover functional tests that spawn     duplicity itself.  Next pass.   - After a run use 'coverage report html' to see     an overview list and links to drill down.  It     shows up in htmlcov/index.html. [kenneth@loafman.com]


## rel.0.8.02 (2019-07-31)

### Other

* Fix dist/makedist to run on python2/3. [kenneth@loafman.com]

* Fix dist/makedist to run on python3. [kenneth@loafman.com]

* Fix dist/makedist to run on python3. [kenneth@loafman.com]

* One last change for bug #1829416 from charlie4096. [kenneth@loafman.com]

* Merged in po-updates. * Fixed bug #1829416 with help from charlie4096   - onedrive: Can’t convert ‘bytes’ object to str implicitly. [kenneth@loafman.com]

* Enhanced build\_duplicity\_test.sh   - Use -h to get help and defaults   - Takes arguments for distro, revno, help   - Distros supported are 18.04, 18.10, 19.04, 19.10   - Revnos are passed to bzr -r option. [kenneth@loafman.com]

* Fix so Docker image duplicity\_test will update and pull   new bzr revisions if changed since last build. [kenneth@loafman.com]

* Remove speedup in testing backup.  The math was correct,   but it's failing on Docker and Launchpad testing. [kenneth@loafman.com]

* Fix language classifiers in setup.py. [kenneth@loafman.com]

* Move pytest-runner setup requirement to a test requirement. [Michael Terry]

* Removed python-gettext from setup.py.  Whoops! [kenneth@loafman.com]

* Merged in lp:\~stragerneds/duplicity/duplicity   - Cache results of filename parsing for speedup. [kenneth@loafman.com]

* Optimize loading backup chains; reduce file\_naming.parse calls. [Matthew Glazar]

* Merged in lp:\~limburgher/duplicity/dropbox   - Fixes bug #1836611 dropbox mixing bytes and strings. [kenneth@loafman.com]

* Correct types for os.join in Dropbox backend. [Gwyn Ciesla]

* Fixed bug #1836829 progress.py: old\_div not defined   - also fixed old\_div in \_boto\_multi.py. [kenneth@loafman.com]

* Fixed bug #1836829 progress.py: old\_div not defined   - also fixed old\_div in \_boto\_multi.py. [kenneth@loafman.com]

* Remove python-gettext from requirements.txt.  Normal   Python installation includes gettext. * Mod README to include Python 3.6 and 3.7. [kenneth@loafman.com]


## rel.0.8.01 (2019-07-14)

### Other

* Merged in po-updates. [kenneth@loafman.com]

* Comment out HSIBackendTest since shim is not up-to-date. [kenneth@loafman.com]

* Install python3.6 and 3.7 explicitly in Dockerfile.  Tox and Docker   now support testing Python 2,7, 3.6, and 3.7. [kenneth@loafman.com]

* Make sure test filenames are bytes not unicode. * Fix test\_glob\_to\_regex to work on Python 3.7. [kenneth@loafman.com]

* Going back to original.  No portable way to ignore warning. [kenneth@loafman.com]

* Another unadorned string. [kenneth@loafman.com]

* Cleanup some trailing spaces/lines in Docker files. [kenneth@loafman.com]

* Fix so we start duplicity with the base python we run under. [kenneth@loafman.com]

* Adjust POTFILES.in for compilec.py move. [kenneth@loafman.com]

* Ensure \_librsync.so is regenned before toc testing. [kenneth@loafman.com]

* Add encoding to logging.FileHandler call to make log file utf8. [kenneth@loafman.com]

* Fix warning in \_librsync.c module. [kenneth@loafman.com]

* Fix some issues found by test\_code.py (try 2) [kenneth@loafman.com]

* Fix some issues found by test\_code.py. [kenneth@loafman.com]

* Fix reversed port assignments (FTP & SSH) in docker-compose.yml. [kenneth@loafman.com]

* Fix reimport problem where "from future.builtins" was being treated   the differently than "from builtins".  They are both the same, so   converted to shorter form "from builtins" and removed duplicates. [kenneth@loafman.com]

* Merged in lp:\~mterry/duplicity/s3fsdecode   - Fix s3 backups by encoding remote filenames. [kenneth@loafman.com]

* Fix s3 backups by encoding remote filenames. [Michael Terry]

* Merged in lp:\~aaron-whitehouse/duplicity/08-dockerfixes   - Update duplicity\_test Dockerfile:     * Use 18.04 instead of 16.04     * Use Ubuntu 18.04 version of pip     * Add Python3 and 2to3 as a dependencies     * Set docker locale as UTF-8. [kenneth@loafman.com]

* Merge with trunk. [Aaron A. Whitehouse]

* Add 2to3 as a dependency to dockerfile. [Aaron A. Whitehouse]

* Add tzdata back in as a dependency and set DEBIAN\_FRONTEND=noninteractive so no tzdata prompt. [Aaron A. Whitehouse]

* Set docker container locale to prevent UTF-8 errors. [Aaron A. Whitehouse]

* Change dockerfile to use 18.04 instead of 16.04 and other fixes. [Aaron A. Whitehouse]

* Merged lp:\~mterry/duplicity/boto-import   - A couple functions in the boto backend were using the boto module     without importing it first. [kenneth@loafman.com]

* Fix s3 backups by importing the boto module. [Michael Terry]

* Normalize shebang to just python, no version number * Fix so most testing/*.py files have the future suggested lines   - from \_\_future\_\_ import print\_function     from future import standard\_library     standard\_library.install\_aliases() [kenneth@loafman.com]

* Fixed failing test in testing/unit/test\_globmatch.py   - Someone is messing with regex.  Fix same.   - See https://bugs.python.org/issue29995 for details. [kenneth@loafman.com]

* Fixed bug #1833559 0.8 test fails with 'duplicity not found' errors   - Fixed assumption that duplicity/rdiffdir were in $PATH. [kenneth@loafman.com]

* Fixed bug #1833573 0.8.00 does not work on Python 2   - Fixed shebang to use /usr/bin/python instead of python2. [kenneth@loafman.com]

* Fix some test\_code errors that slipped by. [kenneth@loafman.com]

* Merged in lp:\~kaffeekiffer/duplicity/azure-python3-fix   - Use util.fsencode to encode file string. [kenneth@loafman.com]

* Fix Azure backend for python 3. [Frank Fischer]

* Fixed bug #1831178 sequence item 0: expected str instance, int found   - Simply converted int to str when making list. [kenneth@loafman.com]

* Fix some import conflicts with the "past" module   - Rename collections.py to dup\_collections.py   - Remove all "from future.utils import old\_div"   - Replace old\_div() with "//" (in py27 for a while).   - All tests run for py3, unit tests run for py3.  The new     import fail is "from future import standard\_library" [kenneth@loafman.com]

* Spaces to tabs for makefile. [Kenneth Loafman]

* Change to python3 for build. [kenneth@loafman.com]

* Merged in lp:\~mterry/duplicity/uexc-string   - The return type of util.uexc should always be a string. [kenneth@loafman.com]

* Have uexc to always return a string. [Michael Terry]

* Add requirements for python-gettext. [kenneth@loafman.com]

* Merged in lp:\~mterry/duplicity/gio-pydrive-fsdecode   - Fix gio and pydrive backends to use fsdecode. [kenneth@loafman.com]

* Fix gio and pydrive backends to use fsdecode. [Michael Terry]

* Merged in lp:\~stragerneds/duplicity/duplicity   - improve test backup speed   - insure all test output is read. [kenneth@loafman.com]

* Remove unnecessary sleeping after running backups in tests. [Matthew Glazar]

* Minimize time spent sleeping between backups. [Matthew Glazar]

* Ensure all duplicity output is captured in tests. [Matthew Glazar]

* Fix TestGlobToRegex.test\_glob\_to\_regex for py3.6 and above   - see https://bugs.python.org/issue29995 for details. [kenneth@loafman.com]

* Some more work on unadorned strings   - Fixed test\_unadorned\_string\_literals to list all strings found   - Added bin/duplicity and bin/rdiffdir to list of files tested   - All unadorned strings have now been adorned. [kenneth@loafman.com]

* Fixed bug #1828662 with patch from Bas Hulsken   - string.split() had been deprecated in 2, removed in 3.7. [kenneth@loafman.com]

* Merged in lp:\~mgorse/duplicity/0.8-series   - Python 3 fixes to imapbackend.py   - Fix bug 1828869: refresh CollectionsStatus after sync. [kenneth@loafman.com]

* Setup.py: allow python 2.7 again. [Mike Gorse]

* Bug #1828869: update CollectionsStatus after sync. [Mike Gorse]

* Imap: python 3 fixes. [Mike Gorse]

* Sync: handle parsed filenames without start/end times. [Mike Gorse]

* More PEP 479 fixes. [Mike Gorse]

* Fix some unadorned strings. [kenneth@loafman.com]

* Fix some unadorned strings. [kenneth@loafman.com]

* Fix to allow >=2.7 or >=3.5. [kenneth@loafman.com]

* Fix to always compile \_librsync before testing. [kenneth@loafman.com]

* Manual merge of lp:\~yajo/duplicity/duplicity   - Support partial metadata sync.   - Fixes bug #1823858 by letting the user to choose partial syncing. Only the metadata for the target chain     will be downloaded. If older (or newer) chains are encrypted with a different passphrase, the user will     be able to restore to a given time by supplying only the passphrase for the chain selected by     the `--restore-time` option when using this new option.   - A side effect is that using this flag reduces dramatically the sync time when moving files from one to     another location, in cases where big amounts of chains are found. [kenneth@loafman.com]

* Change to Python >= 3.5. [kenneth@loafman.com]

* Merged in lp:\~brandon753-ba/duplicity/aws-glacier   - Adds support for for a command line option to store data on AWS S3 Glacier. [kenneth@loafman.com]

* Added documentation on how to use the new AWS S3 Glacier option. [Brandon Anderson]

* Fixed a typo in prior commit. [Brandon Anderson]

* Added support for AWS glacier storage class. [Brandon Anderson]

* Fix bug #1811114 with revised onedrivebackend.py from David Martin   - Adapt to new Microsoft Graph API. [kenneth@loafman.com]

* Removed last mention of copy.com from man page with help from edso. [kenneth@loafman.com]

* Merged in lp:\~aaron-whitehouse/duplicity/08-style-fixes   - Fix pylint style issues (over-indented text, whitespace on blank lines etc)   - Removed "pylint: disable=bad-string-format-type" comment, which was throwing     an error and does not seem to be needed. [kenneth@loafman.com]

* Fix pylint style issues (over-indented text, whitespace on blank lines etc) * Removed "pylint: disable=bad-string-format-type" comment, which was throwing an error and does not seem to be needed. [Aaron A Whitehouse]

* Merged in lp:\~aaron-whitehouse/duplicity/08-uexc-fix   - Fix for Bug #1770929 with associated test cases (thanks to Pete Zaitcev (zaitcev)     in Bug #1797928 for the head start). [kenneth@loafman.com]

* Accomodate unicode input for uexc and add test for this. [Aaron A Whitehouse]

* Convert deprecated .message to args[0] [Aaron A Whitehouse]

* Add test case for lp:1770929 * Added fix (though using deprecated .message syntax) [Aaron A Whitehouse]

* Merged in lp:\~mgorse/duplicity/0.8-series   - More python 3 fixes. [kenneth@loafman.com]

* Attempt to port sx backend to python 3. [Mike Gorse]

* Rsync: py3 fixes. [Mike Gorse]

* Ncftp: py3 fixes. [Mike Gorse]

* Test\_selection.py: fix an invalid escape sequence on py3. [Mike Gorse]

* Fix sync\_archive on python 3. [Mike Gorse]

* Ssh\_pexpect: py3 fixes. [Mike Gorse]

* Pull from main branch. [Mike Gorse]

* Fixed bug #1817375 with hint from mgorse   - Added 'global pexpect' at end of imports. [kenneth@loafman.com]


