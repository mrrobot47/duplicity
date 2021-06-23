#!/bin/sh
set -x -e

for ((x=0 ; x<100 ; x++)); do
    echo "\nLoop $x\n"

    # ----- cleanup -----
    rm -r /Volumes/home/testdup

    # ----- making initial backup -----
    PYTHONPATH=. bin/duplicity --no-encr --no-print -v0 --name=foo /usr/bin file:///Volumes/home/testdup --volsize=2 &
    pid=$!
    sleep 10

    # ----- kill after 10 seconds ------
    kill -9 $pid
    sleep 1

    # ----- restarting first backup -----
    PYTHONPATH=. bin/duplicity --no-encr --no-print -v0 --name=foo /usr/bin file:///Volumes/home/testdup --volsize=2

    # ----- verifying backup -----
    PYTHONPATH=. bin/duplicity verify --no-encr --name=foo file:///Volumes/home/testdup /usr/bin --volsize=2

    if [ $# != 0 ] ; then
    echo "----- Guh!  We hit the bug! -----"
    exit $#
    else
    echo "----- Yay!  We didn't hit the bug! -----"
    fi
done
