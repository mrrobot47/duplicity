#!/bin/bash

set -e

cd `dirname $0`/../..

export PYTHONPATH=`pwd`
export PASSPHRASE=""
export MYTESTKEY=2D7CDA824BB7660CDE350B228C2938CE3CAEB354

# Clean up
rm -rf /tmp/testfiles /tmp/testbackup ~/.cache/duplicity/mytestbackup

ulimit -n 102400

mkdir /tmp/testfiles
mkdir /tmp/testbackup

# Full backup plus 253 incremental backups
for i in {1..254}
do
    dd if=/dev/urandom of=/tmp/testfiles/test${i}.file bs=1M count=1
    bin/duplicity --name mytestbackup --encrypt-key ${MYTESTKEY} /tmp/testfiles par2+file:///tmp/testbackup
done

# verify works
bin/duplicity verify --name mytestbackup --encrypt-key ${MYTESTKEY} par2+file:///tmp/testbackup /tmp/testfiles

# 255th backup set
dd if=/dev/urandom of=/tmp/testfiles/test255.file bs=1M count=1
bin/duplicity --name mytestbackup --encrypt-key ${MYTESTKEY} /tmp/testfiles par2+file:///tmp/testbackup

# verify crashes with "filedescriptor out of range in select()"
bin/duplicity verify -v9 --name mytestbackup --encrypt-key ${MYTESTKEY} par2+file:///tmp/testbackup /tmp/testfiles

# Clean up
rm -r /tmp/testfiles /tmp/testbackup ~/.cache/duplicity/mytestbackup
