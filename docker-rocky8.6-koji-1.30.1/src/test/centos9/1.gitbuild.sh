#!/bin/bash

set -x

koji build centos9-addons --skip-tag  --nowait   'git+https://git.centos.org/rpms/bash#origin/c9'

exit 0


