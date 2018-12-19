#!/bin/bash
set -e
set -x

BUCKET=s3://courses.diveintodeeplearning.org/berkeley-stat-157
DIR=_build/html/

aws s3 sync --delete $DIR $BUCKET --acl 'public-read'
