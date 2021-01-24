# REPO README - Notes for people checking out of GitLab (git)

## Getting duplicity to run:

By the numbers:
1. Do the checkout to a location called $DUP_ROOT:
   - `git clone git@gitlab.com:duplicity/duplicity.git $DUP_ROOT` or
   - `git clone https://gitlab.com/duplicity/duplicity.git $DUP_ROOT`
2. Build the extension module
   - `cd $DUP_ROOT`
   - `setup.py build_ext`
3. Run `PYTHONPATH=$DUP_ROOT bin/duplicity -V`. You will see
   "duplicity $version" instead of the normal version number.
   Versioning comes during the release.

Use PYTHONPATH to set the path each time that you use the binaries:

`PYTHONPATH=$DUP_ROOT bin/duplicity`

or

`PYTHONPATH=$DUP_ROOT bin/rdiffdir`
