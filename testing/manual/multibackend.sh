#!/bin/bash

cd `dirname $0`/../..

export PYTHONPATH=`pwd`:$PYTHONPATH

#export PYDEVD=True
python3 bin/duplicity ../duplicity-web multi:///`pwd`/testing/manual/multibackend.json?mode=mirror
python2 bin/duplicity ../duplicity-web multi:///`pwd`/testing/manual/multibackend.json?mode=mirror
