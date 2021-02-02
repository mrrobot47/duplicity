# INSTALLATION

Thank you for trying duplicity.  To install, run:

```
python setup.py install
```

The build process can be also be run separately:

```
python setup.py build
```

The default prefix is /usr, so files are put in /usr/bin,
/usr/share/man/, etc.  An alternate prefix can be specified using the
--prefix=<prefix> option.  For example:

```
python setup.py install --prefix=/usr/local
export PYTHONPATH='/usr/local/lib/python.x/site-packages/'
/usr/local/bin/duplicity -V`
```

# REQUIREMENTS

 * Python 2.7, or 3.5 to 3.9
 * librsync v0.9.6 or later
 * GnuPG for encryption
 * fasteners 0.14.1 or later for concurrency locking
 * for scp/sftp -- python-paramiko
 * for ftp -- lftp version 3.7.15 or later
 * Boto 2.0 or later for single-processing S3 or GCS access (default)
 * Boto 2.1.1 or later for multi-processing S3 access
 * Boto 2.7.0 or later for Glacier S3 access
 * Boto3 1.15 or later for S3

If you install from the source package, you will also need:

 * Python development files, normally found in module 'python-dev'.
 * librsync development files, normally found in module 'librsync-dev'.


# DEVELOPMENT

For more information on downloading duplicity's source code from the
code repository and developing for duplicity, see README-REPO.

# HELP

For more information see the duplicity home page at:

  http://www.nongnu.org/duplicity

or post to the mailing list at

  https://lists.nongnu.org/mailman/listinfo/duplicity-talk
