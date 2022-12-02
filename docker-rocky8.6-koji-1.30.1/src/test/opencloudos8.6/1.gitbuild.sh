#!/bin/bash

set -x

koji build opencloudos8.6-addons --skip-tag  --nowait   'git+https://gitee.com/src-opencloudos-rpms/bash#origin/oc8'

exit 0
