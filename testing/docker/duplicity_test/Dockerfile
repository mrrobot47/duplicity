# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4; encoding:utf8 -*-
#
# Copyright 2019 Nils Tekampe <nils@tekampe.org>,
# Kenneth Loafman <kenneth@loafman.com>,
# Aaron Whitehouse <code@whitehouse.kiwi.nz>
#
# This file is part of duplicity.
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

FROM ubuntu:20.04

# Set locale to prevent UTF-8 errors
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYENV_ROOT "/root/.pyenv"
ENV PATH "$PYENV_ROOT/bin:$PYENV_ROOT/shims:$PATH"
ENV TOXWORKDIR="/root/.tox"

# Set to non-interactive so no tzdata prompt
ARG DEBIAN_FRONTEND=noninteractive

# Installing some pre-requisites and some
# packages needed for testing duplicity
RUN apt-get update \
    && apt-get install -y \
        2to3 \
        build-essential \
        git \
        intltool \
        lftp \
        librsync-dev \
        libffi-dev \
        libssl-dev \
        openssl \
        par2 \
        python3-pip \
        python3 \
        rdiff \
        tzdata \
# The following packages are for building python via pyenv
    && apt-get install -y \
        curl \
        libbz2-dev \
        libffi-dev \
        liblzma-dev \
        libncursesw5-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        libxml2-dev \
        libxmlsec1-dev \
        llvm \
        make \
        tk-dev \
        wget \
        xz-utils \
        zlib1g-dev \
# The following packages are not necessary for testing but make life easier or support debugging
    && apt-get install -y \
        ftp \
        iputils-ping \
        mc \
        nano \
        net-tools \
        rsync \
    && rm -rf /var/lib/apt/lists/*

# Install pyenv
RUN git clone -b "v2.3.0" --single-branch https://github.com/pyenv/pyenv.git /root/.pyenv \
    && eval "$(pyenv init --path)" \
    && eval "$(pyenv init -)" \
# Install all the Pythons we test
    && pyenv install 2.7.18 \
    && pyenv install 3.5.10 \
    && pyenv install 3.6.15 \
    && pyenv install 3.7.13 \
    && pyenv install 3.8.13 \
    && pyenv install 3.9.11 \
    && pyenv install 3.10.3

# Tell tox how to find executables, install all requirements
COPY requirements.dev .
COPY requirements.txt .
COPY tox.ini .
RUN python3 -m pip install --upgrade pip setuptools setuptools-scm \
    && python3 -m pip install -rrequirements.dev -rrequirements.txt \
    && python3 -m pip install tox tox-pyenv \
    && pyenv local 2.7.18 3.5.10 3.6.15 3.7.13 3.8.13 3.9.11 3.10.3

# set up tiny dummy project to make tox happy
WORKDIR /root
COPY hello-world-master.zip .
RUN unzip -o hello-world-master.zip
COPY requirements.dev hello-world-master
COPY requirements.txt hello-world-master
COPY tox.ini hello-world-master

# set to dummy workdir
WORKDIR /root/hello-world-master

# run tox so environss are created as part of image.
RUN tox --notest -- --setup-only

# cleanup the noise left over
RUN rm -rf /root/.tox/dist/hello_world*.zip \
    rm -rf /root/.tox/distshare/hello_world*.zip \
    rm -rf /root/hello-world-master* \
    rm -rf /root/requirements.* \
    rm -rf /root/tox.ini

# Set workdir to duplicity
WORKDIR /root/duplicity
