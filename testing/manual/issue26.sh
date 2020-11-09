#!/bin/bash

cd `dirname $0`/../..

export PYTHONPATH=`pwd`
export PASSPHRASE=foo

alias python3=python3.9

bin/duplicity full ../duplicity-web par2+file:///tmp/testdup
sleep 1
bin/duplicity full ../duplicity-web par2+file:///tmp/testdup
sleep 1
bin/duplicity full ../duplicity-web par2+file:///tmp/testdup
sleep 1

export PYDEVD=True
bin/duplicity remove-all-but-n-full 1 --force --num-retries=1 -v9 par2+file:///tmp/testdup

ls -l /tmp/testdup
rm -rf /tmp/testdup
