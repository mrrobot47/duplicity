#!/bin/bash

cd `dirname $0`/../..

export PYTHONPATH=`pwd`

alias python3=python3.9

#export PYDEVD=True

rm -rf /tmp/issue100 ~/.cache/duplicity/issue100

bin/duplicity full -v9 --no-enc --name=issue100 --fail=1 /etc file:///tmp/issue100
ls -l /tmp/issue100 ~/.cache/duplicity/issue100

bin/duplicity cleanup -v9 --force --no-enc --name=issue100 file:///tmp/issue100
ls -l /tmp/issue100 ~/.cache/duplicity/issue100
