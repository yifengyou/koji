#!/bin/bash

set -x

koji build centos8-addons --skip-tag  --nowait   'git+https://git.centos.org/rpms/python-flask#origin/c8'

exit 0


koji build centos8-addons --skip-tag  --nowait   'git+https://git.centos.org/rpms/bash#origin/c8'
koji build centos8-addons --skip-tag  --nowait   'git+https://git.centos.org/rpms/cockpit#origin/c8'

