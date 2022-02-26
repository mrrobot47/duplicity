#!/bin/bash

cd `dirname $0`/../..

export PYTHONPATH=`pwd`
BASE=/Volumes/home/issue110

rm -rf ${BASE}/backup
mkdir -p ${BASE}/backup

bin/duplicity --no-encryption \
    --verbosity=info \
    --name=issue110 \
    --volsize=1024 \
    ${BASE}/000 \
    file://${BASE}/backup
