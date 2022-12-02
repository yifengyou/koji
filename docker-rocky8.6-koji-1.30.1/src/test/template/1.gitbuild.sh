#!/bin/bash

set -x

koji mock-config --target build rockylinux8.6-addons -a x86_64


koji build rockylinux8.6-addons --skip-tag  --nowait   'git+https://git.centos.org/rpms/python-flask#origin/c8'

exit 0
exit 0

koji build rockylinux8.6-addons --skip-tag  --nowait   'git+https://git.centos.org/rpms/bash#origin/c8'
koji build rockylinux8.6-addons --skip-tag  --nowait   'git+https://git.centos.org/rpms/cockpit#origin/c8'
https://git.centos.org/rpms/cockpit
