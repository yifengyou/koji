#!/bin/bash

set -x

koji build rockylinux8.6-addons rocky-release-8.7-1.2.el8.src.rpm --skip-tag

#koji build rockylinux8.6-addons bash-4.4.20-4.el8_6.src.rpm --skip-tag
#koji build rockylinux8.6-addons passwd-0.80-4.el8.src.rpm --skip-tag

exit 0
koji build rockylinux8.6-addons curl-7.61.1-25.el8.src.rpm --skip-tag
