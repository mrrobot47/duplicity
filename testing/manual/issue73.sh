source ~/swift-auth.env

dd if=/dev/zero of=/tmp/testfile bs=1000000 count=100

echo Running duplicity without multipart
duplicity \
  --full-if-older-than 30D --verbosity 9 \
  --name home --no-encryption \
  /tmp/testfile swift://issue73

duplicity \
  --full-if-older-than 30D --verbosity 9 \
  --name home --no-encryption --volsize 20 \
  --mp-segment-size 10 \
  --no-compression \
  /tmp/testfile swift://issue73-2


