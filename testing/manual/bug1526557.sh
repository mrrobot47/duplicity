#!/bin/bash

export PATH=/usr/local/bin:/usr/local/sbin:$PATH
export PYTHONPATH='.':$PYTHONPATH
PASSPHRASE=foo bin/duplicity full ~/workspace/duplicity-web file:///tmp/testdup/ --name=testdup
touch ~/workspace/duplicity-web/index.wml
PASSPHRASE=foo bin/duplicity inc ~/workspace/duplicity-web file:///tmp/testdup/ --name=testdup
PASSPHRASE=foo bin/duplicity coll file:///tmp/testdup/ --name=testdup
PASSPHRASE=foo bin/duplicity coll --file-changed=index.wml file:///tmp/testdup/ --name=testdup --pydevd
