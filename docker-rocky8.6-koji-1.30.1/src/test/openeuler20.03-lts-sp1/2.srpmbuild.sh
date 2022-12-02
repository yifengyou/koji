#!/bin/bash

set -x

yumdownloader --source centos-release
koji build openeuler20.03-lts-sp1-addons centos-release*.src.rpm --skip-tag

exit 0

