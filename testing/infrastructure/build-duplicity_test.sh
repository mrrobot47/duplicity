#!/bin/bash

cd ../..
docker build --tag firstprime/duplicity_test:latest -f testing/infrastructure/duplicity_test/Dockerfile .

cd testing/infrastructure/ftp_server
docker build --tag firstprime/duplicity_ftp:latest .
cd ..

cd ssh_server
cp -p ../id_rsa.pub .
docker build --tag firstprime/duplicity_ssh:latest .
rm id_rsa.pub
cd ..
