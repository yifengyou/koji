#!/bin/bash

set -x

koji build centos7-addons --skip-tag  --nowait   'git+https://git.centos.org/rpms/python-flask#origin/c7'

exit 0


koji build centos7-addons --skip-tag  --nowait   'git+https://git.centos.org/rpms/bash#origin/c7'
koji build centos7-addons --skip-tag  --nowait   'git+https://git.centos.org/rpms/cockpit#origin/c7'

