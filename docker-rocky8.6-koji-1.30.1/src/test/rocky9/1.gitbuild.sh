#!/bin/bash

set -x

koji mock-config --target rockylinux9-addons -a x86_64

koji build rockylinux9-addons --skip-tag  --nowait   'git+https://git.rockylinux.org/staging/src/rocky-release#origin/r9'

exit 0

koji build rockylinux9-addons --skip-tag  --nowait   'git+https://git.rockylinux.org/staging/rpms/pytest#origin/r9'

koji build rockylinux9-addons --skip-tag  --nowait   'git+https://git.rockylinux.org/staging/rpms/python-jinja2#origin/r9'

koji build rockylinux9-addons --skip-tag  --nowait   'git+https://git.rockylinux.org/staging/rpms/python-flask#origin/r9'

