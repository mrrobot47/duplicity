#!/bin/sh
[ -z "$SNAP" ] && {
  echo Missing env var SNAP.
  exit 1
}
"$SNAP"/bin/$(basename "${0%.sh}") "$@"
