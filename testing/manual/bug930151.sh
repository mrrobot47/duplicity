#!/bin/bash

rm -rf /tmp/duplicity /tmp/backup /tmp/foo foo

DUPDIR=`pwd`

mkdir -p /tmp/duplicity
cd /tmp/duplicity/

touch /tmp/foo
ln -s /tmp/foo foo

ls -l /tmp/foo foo

echo "umask: `umask`"

PYTHONPATH=${DUPDIR} ${DUPDIR}/bin/duplicity -v0 --no-print --no-enc /tmp/duplicity/ file:///tmp/backup

rm foo

PYDEVD=1 PYTHONPATH=${DUPDIR} ${DUPDIR}/bin/duplicity -v9 --no-enc --file-to-restore foo file:///tmp/backup /tmp/duplicity/foo

ls -l /tmp/foo foo
