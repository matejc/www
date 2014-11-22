#!/bin/bash

BASEDIR="$(dirname $(readlink -f $0))"

status=0

strip_comments() { awk '/^ *[^# ]/{print $1}' "$1"; }

packages="$(strip_comments "$BASEDIR/linux-packages.txt")"
if command -v sudo apt-get >/dev/null; then
    sudo apt-get -qq -y install python-pip $packages
else
    echo "Warning: sudo apt-get unavailable. Please manually install common packages: $packages"
    status=1
fi

if command -v pip >/dev/null; then
    pip install --upgrade --use-mirrors --requirement "$BASEDIR/requirements.txt"
else
    echo "Warning: pip unavailable. Please install python packages from bin/requirements.txt"
    status=1
fi

exit $status
