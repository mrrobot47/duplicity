#!/bin/bash

cd `dirname $0`/../..

export PYTHONPATH=`pwd`
export PASSPHRASE=foo

#export PYDEVD=True

for t in 'mirror' 'stripe'; do
    for i in $(seq 10); do
        bin/duplicity --no-encryption full /etc/hosts "multi:///`pwd`/testing/manual/bug1919017.json?mode=$t"
        sleep 1
    done

    bin/duplicity --verbosity 9 --no-encryption remove-all-but-n-full 1 "multi:///`pwd`/testing/manual/issue25.json?mode=$t" --force 2>&1 | grep 'failed to delete'

    ls -l /tmp/*_drive

    rm -rf /tmp/*_drive
done
