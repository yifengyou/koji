#!/bin/bash

set -x

koji mock-config --target  openeuler20.03-lts-sp1-addons -a x86_64

echo "=========================================================================="

koji build openeuler20.03-lts-sp1-addons --skip-tag  --nowait   'git+https://gitee.com/src-openeuler/openEuler-release#origin/openEuler-20.03-LTS-SP1'

exit 0

koji build openeuler20.03-lts-sp1-addons --skip-tag  --nowait   'git+https://gitee.com/src-openeuler/bash#origin/openEuler-20.03-LTS-SP1'

