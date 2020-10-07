#!/bin/sh

export PASSPHRASE=foo
export PYTHONPATH=../../../

rm -rf /tmp/testdup /tmp/testrest

$PYTHONPATH/bin/duplicity full -v5 data file:///tmp/testdup
$PYTHONPATH/bin/duplicity list-current-files -v5 file:///tmp/testdup
$PYTHONPATH/bin/duplicity verify --compare-data -v5 file:///tmp/testdup data
$PYTHONPATH/bin/duplicity inc -v5 data file:///tmp/testdup
$PYTHONPATH/bin/duplicity restore -v5 file:///tmp/testdup /tmp/testrest

diff data /tmp/testrest
echo "diff returned $?"
