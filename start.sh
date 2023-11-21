#!/bin/bash
pushd $BETTER_WYZE_ROOT
source .venv/bin/activate
pushd src
python serve.py

