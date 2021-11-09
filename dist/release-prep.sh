#!/bin/bash

set -e

if [ "$1" != "" ]; then
    REL=$1
else
    echo "usage: $0 version"
    exit 1
fi

echo "Prepping for release ${REL}"

while true; do
    read -n 1 -p "Is ${REL} the correct version (y/n)?" yn
    case $yn in
        [Yy]* ) echo; break;;
        [Nn]* ) echo; exit;;
        * ) echo "Please answer yes or no.";;
    esac
done

if [ `uname` == "Darwin" ]; then
    SED=gsed
else
    SED=sed
fi

set -v

# put in correct version for Launchpad
${SED} -i s/${REL}.dev/${REL}/g setup.py
git commit -a -m"Prep for ${REL}"

# add release tag and push it
git tag -f rel.${REL}
git push --tags -f origin master -o ci.skip

# make changelog and move tag to include it
dist/makechangelog
git tag -f rel.${REL}
git push --tags -f origin master

# update all repos
git push mirror master
git push alpha master -o ci.skip

# make and sign the release
./setup.py sdist --dist-dir=.
gpg --use-agent -b duplicity-${REL}.tar.gz

# release tar/sig to Savannah
scp duplicity-${REL}.* loafman@dl.sv.nongnu.org:/releases/duplicity/

# move releases to duplicity-releases
mv duplicity-${REL}.* ../duplicity-releases
