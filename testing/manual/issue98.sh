#!/bin/bash -v

cd `dirname $0`/../..

export PYTHONPATH=`pwd`

alias python3=python3.9

#export PYDEVD=True

rm -rf ~/.cache/duplicity/issue98 /tmp/first_drive /tmp/second_drive

bin/duplicity \
    full \
    --name issue98 \
    --volsize 5 \
    --no-encryption \
    ../duplicity-web-git \
    file:///tmp/first_drive

bin/duplicity \
    inc \
    --name issue98 \
    --volsize 5 \
    --no-encryption \
    ../duplicity-web-git \
    file:///tmp/first_drive

bin/duplicity \
    replicate \
    --name issue98 \
    --volsize 5 \
    --no-encryption \
    --verbosity 9 \
    file:///tmp/first_drive \
    file:///tmp/second_drive

bin/duplicity \
    verify \
    --name issue98 \
    --volsize 5 \
    --no-encryption \
    file:///tmp/first_drive \
    ../duplicity-web-git

bin/duplicity \
    verify \
    --name issue98 \
    --volsize 5 \
    --no-encryption \
    file:///tmp/second_drive \
    ../duplicity-web-git

ls -l ~/.cache/duplicity/issue98 /tmp/first_drive /tmp/second_drive
