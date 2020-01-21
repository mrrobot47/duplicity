#!/bin/bash -v

export PYTHONPATH='.'

cat > /tmp/multi.json <<"EOF"
[
  {
   "url": "file:///tmp/fragile"
  },
  {
   "url": "file:///tmp/solid"
  }
]
EOF

bin/duplicity --no-encryption /bin/ 'multi:///tmp/multi.json?mode=mirror'

# corrupt the first target

cat > /tmp/multi.json <<"EOF"
[
  {
   "url": "file:///xtmp/fragile"
  },
  {
   "url": "file:///tmp/solid"
  }
]
EOF

bin/duplicity list-current-files multi:///tmp/multi.json

# corrupt the first target so that it can still be written to

cat > /tmp/multi.json <<"EOF"
[
  {
   "url": "file:///tmp/fragile.new"
  },
  {
   "url": "file:///tmp/solid"
  }
]
EOF

bin/duplicity list-current-files multi:///tmp/multi.json

