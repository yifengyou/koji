#!/bin/bash

set -x

koji add-tag openeuler20.03-lts-sp1-base
koji add-tag openeuler20.03-lts-sp1-base-addon
koji add-tag openeuler20.03-lts-sp1-base-addon-testing --parent=openeuler20.03-lts-sp1-base-addon
koji add-tag openeuler20.03-lts-sp1-addons-build --parent=openeuler20.03-lts-sp1-base-addon --arches="x86_64"
koji add-tag-inheritance --priority=1 openeuler20.03-lts-sp1-addons-build openeuler20.03-lts-sp1-base

koji add-external-repo -t openeuler20.03-lts-sp1-base -m bare openeuler20.03-lts-sp1-everything        https://repo.huaweicloud.com/openeuler/openEuler-20.03-LTS-SP1/everything/x86_64/
koji add-external-repo -t openeuler20.03-lts-sp1-base -m bare openeuler20.03-lts-sp1-update            https://repo.huaweicloud.com/openeuler/openEuler-20.03-LTS-SP1/update/x86_64/

koji add-group openeuler20.03-lts-sp1-addons-build build
koji add-group openeuler20.03-lts-sp1-addons-build srpm-build

koji add-group-pkg openeuler20.03-lts-sp1-addons-build   build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch openEuler-rpm-config openEuler-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz
koji add-group-pkg openeuler20.03-lts-sp1-addons-build   srpm-build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch openEuler-rpm-config openEuler-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz

koji add-target openeuler20.03-lts-sp1-addons openeuler20.03-lts-sp1-addons-build openeuler20.03-lts-sp1-base-addon-testing


echo "All done!"

exit 0


koji add-external-repo -t openeuler20.03-lts-sp1-base -m bare openeuler20.03-lts-sp1-debuginfo         https://repo.huaweicloud.com/openeuler/openEuler-20.03-LTS-SP1/debuginfo/x86_64/
