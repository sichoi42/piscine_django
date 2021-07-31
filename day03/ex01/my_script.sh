#!/bin/sh

python3 -m pip --version

mkdir -p local_lib

python3 -m venv local_lib

source local_lib/bin/activate

pip install -t local_lib --log install.log --force-reinstall git+https://github.com/jaraco/path.py.git

python3 my_program.py
