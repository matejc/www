#!/bin/bash

BASEDIR="$(dirname $(readlink -f $0))"

status=0

strip_comments() { awk '/^ *[^# ]/{print $1}' "$1"; }

packages="$(strip_comments "$BASEDIR/depends/linux-packages.txt")"
if command -v sudo apt-get >/dev/null; then
    sudo apt-get -qq -y install python-pip $packages
else
    echo "Warning: sudo apt-get unavailable. Please manually install common packages: $packages"
    status=1
fi

if command -v pip >/dev/null; then
    pip install --upgrade --use-mirrors --requirement "$BASEDIR/depends/requirements.txt"
else
    echo "Warning: pip unavailable. Please install python packages from depends/requirements.txt"
    status=1
fi

exit $status

if command -v git >/dev/null; then
    for repo in $(strip_comments "$BASEDIR/depends/github-repos.txt"); do
        git clone --recursive https://github.com/$repo.git
    done
else
    echo "Warning: git unavailable. Please clone github repositories from depends/github-repos.txt"
    status=1
fi
