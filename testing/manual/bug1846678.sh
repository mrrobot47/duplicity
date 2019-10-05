#!/bin/bash

mkdir -p /tmp/duplicity-test
cd /tmp/duplicity-test/
mkdir a
mkdir b
touch a/one
touch a/two

PASSPHRASE=password duplicity --exclude-device-files a/ file:///tmp/duplicity-test/b
