#!/bin/bash

set -x

yumdownloader --source centos-release
koji build centos7-addons centos-release*.src.rpm --skip-tag

exit 0

