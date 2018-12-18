#!/bin/bash
set -e

git submodule update --init
conda env create -f environment.yml
conda activate berkeley-stat-157

make html
