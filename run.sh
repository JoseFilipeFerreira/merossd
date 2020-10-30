#!/bin/bash
git pull

if [ -e '.env' ]; then
    source '.env/bin/activate'
else
    virtualenv '.env' || exit 2
    source '.env/bin/activate' || exit 3
    pip install -r 'requirements.txt' --upgrade || exit 4
fi

while true; do
    rm -f /tmp/meross.daemon
    python meross.py
done
