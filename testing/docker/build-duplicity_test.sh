#!/bin/bash
#
# Copyright 2019 Nils Tekampe <nils@tekampe.org>,
# Kenneth Loafman <kenneth@loafman.com> and Aaron Whitehouse <code@whitehouse.kiwi.nz>
#
# This file is part of duplicity.
# This script sets up a test network for the tests of dupclicity
# This script takes the assumption that the containers for the testinfrastructure do deither run
# or they are removed. It is not intended to have stopped containers.
#
# Duplicity is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# Duplicity is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with duplicity; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

usage() {
    echo "Usage: $0 [-d <distro>]" 1>&2
    echo "  - Default distro is 18.04" 1>&2
    exit 1;
}

# set defaults if not in environment

if [ "$DISTRO" == "" ]; then
    DISTRO=18.04
fi

# possibly override with commandline

while getopts ":d:h" opt; do
    case ${opt} in
        d )
            DISTRO=$OPTARG
            ;;
        h )
            usage
            ;;
        \? )
            echo "Invalid option: $OPTARG" 1>&2
            usage
            ;;
        : )
            echo "Invalid option: $OPTARG requires an argument" 1>&2
            usage
        ;;
    esac
done
shift $((OPTIND -1))

# build duplicity_test

cd `dirname $0`/duplicity_test
cp -p ../../../requirements.txt .
cp -p ../id_rsa* .
mkdir dupcopy
rsync -a \
    --exclude=*.py[co] \
    --exclude=*.so \
    --exclude=.DS_Store \
    --exclude=.git \
    --exclude=.tox \
    --exclude=S.* \
    --exclude=__pycache__ \
    --exclude=htmlcov \
    ../../../ \
    dupcopy/
docker build -f Dockerfile-$DISTRO --tag firstprime/duplicity_test .
rm requirements.txt id_rsa*
rm -r dupcopy

# build duplicity_ftp

cd ../ftp_server
docker build --tag firstprime/duplicity_ftp .

# build duplicity_ssh

cd ../ssh_server
cp -p ../id_rsa.pub .
docker build --tag firstprime/duplicity_ssh .
rm id_rsa.pub
