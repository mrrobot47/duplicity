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


## Getting a versioned copy of duplicity

Duplicity source is versioned by **git tags** and **setuptools-scm** with help from `./setup.py sdist --dist-dir=.`.
The following should suffice to give you versioned source.

So, for version 0.8.21:
```
git clone --branch rel.0.8.21 git@gitlab.com:duplicity/duplicity.git
```
will produce a working git directory **duplicity** in the current directory.
```
cd duplicity
./setup.py sdist --dist-dir=.
tar xf duplicity-0.8.21.tar.gz
```
will produce a versioned source in **duplicity-0.8.21**

Then just run
```
cd duplicity-8.8,21
./setup.py build
```
or
```
cd duplicity-0.8.21
./setup.py install
```
as needed.
