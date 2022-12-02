#!/bin/bash

set -x

yumdownloader --source rocky-release

koji build anolis8-addons rocky-release-8.7-1.2.el8.src.rpm --skip-tag

exit 0

#koji build anolis8-addons bash-4.4.20-4.el8_6.src.rpm --skip-tag
#koji build anolis8-addons passwd-0.80-4.el8.src.rpm --skip-tag
koji build anolis8-addons curl-7.61.1-25.el8.src.rpm --skip-tag
