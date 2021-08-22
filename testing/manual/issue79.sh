#!/bin/bash

cd `dirname $0`/../..

export PYTHONPATH=`pwd`
export PASSPHRASE=foo

alias python3=python3.9

#export PYDEVD=True

for MODE in mirror stripe; do

    echo "----- Testing ${MODE} mode -----\n"

    rm -rf /tmp/first_drive /tmp/second_drive

    bin/duplicity full ../duplicity-web multi:///`pwd`/testing/manual/issue79.json?mode=${MODE}
    bin/duplicity full ../duplicity-web multi:///`pwd`/testing/manual/issue79.json?mode=${MODE}
    bin/duplicity full ../duplicity-web multi:///`pwd`/testing/manual/issue79.json?mode=${MODE}
    bin/duplicity full ../duplicity-web multi:///`pwd`/testing/manual/issue79.json?mode=${MODE}
    bin/duplicity full ../duplicity-web multi:///`pwd`/testing/manual/issue79.json?mode=${MODE}

    bin/duplicity remove-all-but-n-full 1 --force multi:///`pwd`/testing/manual/issue79.json?mode=${MODE}
    bin/duplicity collection-status multi:///`pwd`/testing/manual/issue79.json?mode=

done
