#!/bin/bash
set -e

git submodule update --init
conda env update -f build/environment.yml
# you may need to change to
# source activate berkeley-stat-157
conda activate berkeley-stat-157

make clean
make html
