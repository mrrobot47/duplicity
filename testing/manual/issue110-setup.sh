#!/bin/bash

BASE=${HOME}/issue110
DATA=${HOME}/random_data

dd if=/dev/urandom of=${DATA} bs=1 count=$(( 65 * 1024 )) >& /dev/null

mkdir -p ${BASE}/000
cd ${BASE}/000

for i in {0..9}; do
    mkdir -p $(printf "dir_i_%03d" $i)
    cd $(printf "dir_i_%03d" $i)
    for j in {0..999}; do
        mkdir -p $(printf "dir_j_%03d" $j)
        cd $(printf "dir_j_%03d" $j)
        for k in {0..999}; do
            dd if=${DATA} of=$(printf "file_%03d" $k) bs=$(( RANDOM + 1024 )) count=1 >& /dev/null
        done
        cd ..
    done
    cd ..
done
cd ..
