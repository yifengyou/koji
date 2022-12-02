#!/bin/bash

set -x

yumdownloader --source opencloudos-release

koji build opencloudos8.6-addons opencloudos-release*.src.rpm --skip-tag

exit 0

