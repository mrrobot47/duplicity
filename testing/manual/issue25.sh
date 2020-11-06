#!/bin/bash

cd `dirname $0`/../..

export PYTHONPATH=`pwd`
export PASSPHRASE=foo

alias python3=python3.9

#export PYDEVD=True
bin/duplicity full ../duplicity-web multi:///`pwd`/testing/manual/issue25.json?mode=mirror
bin/duplicity full ../duplicity-web multi:///`pwd`/testing/manual/issue25.json?mode=mirror
bin/duplicity full ../duplicity-web multi:///`pwd`/testing/manual/issue25.json?mode=mirror
bin/duplicity full ../duplicity-web multi:///`pwd`/testing/manual/issue25.json?mode=mirror
bin/duplicity full ../duplicity-web multi:///`pwd`/testing/manual/issue25.json?mode=mirror

bin/duplicity remove-all-but-n-full 1 --force multi:///`pwd`/testing/manual/issue25.json?mode=mirror
