#!/bin/sh

mkdir -p django_venv

python3 -m venv django_venv

source django_venv/bin/activate

python3 -m pip install --requirement requirement.txt

