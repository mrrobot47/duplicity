#!/bin/sh
set -x -e

SOURCE=/usr/bin
TARGET=/Volumes/home/testdup
OPTS="--no-encr --no-comp -v0 --no-print --volsize=2 --name=foo"

for ((x=0 ; x<100 ; x++)); do
    echo "\nLoop $x\n"

    # ----- cleanup -----
    rm -r ${TARGET}

    # ----- making initial backup -----
    PYTHONPATH=. bin/duplicity full ${OPTS} ${SOURCE} file://${TARGET} &
    pid=$!
    sleep 10

    # ----- kill after 10 seconds ------
    kill -9 $pid
    sleep 1
    echo "killed while writing: $(ls -rt /Volumes/home/testdup/ | tail -1)"

    # ----- restarting first backup -----
    PYTHONPATH=. bin/duplicity full ${OPTS} --name=foo ${SOURCE} file://${TARGET}

    # ----- verifying backup -----
    PYTHONPATH=. bin/duplicity verify ${OPTS} file://${TARGET} ${SOURCE}

    if [ $# != 0 ] ; then
        echo "----- Guh!  We hit the bug! -----"
        exit $#
    else
        echo "----- Yay!  ALL OK! -----"
    fi
done
