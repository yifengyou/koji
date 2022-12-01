#!/bin/bash

set -x

koji add-tag anolis8-base
koji add-tag anolis8-base-addon
koji add-tag anolis8-base-addon-testing --parent=anolis8-base-addon
koji add-tag anolis8-addons-build --parent=anolis8-base-addon --arches="x86_64"
koji add-tag-inheritance --priority=1 anolis8-addons-build anolis8-base

koji add-external-repo -t anolis8-base -m bare anolis8-AppSteam          http://mirrors.aliyun.com/anolis/8/AppStream/\$arch/os/
koji add-external-repo -t anolis8-base -m bare anolis8-BaseOs            http://mirrors.aliyun.com/anolis/8/BaseOS/\$arch/os/
koji add-external-repo -t anolis8-base -m bare anolis8-Extras            http://mirrors.aliyun.com/anolis/8/Extras/\$arch/os/
koji add-external-repo -t anolis8-base -m bare anolis8-PowerTools        http://mirrors.aliyun.com/anolis/8/PowerTools/\$arch/os/
koji add-external-repo -t anolis8-base -m bare anolis8-HighAvailability  http://mirrors.aliyun.com/anolis/8/HighAvailability/\$arch/os/
koji add-external-repo -t anolis8-base -m bare anolis8-Plus              http://mirrors.aliyun.com/anolis/8/Plus/\$arch/os/
koji add-external-repo -t anolis8-base -m bare anolis8-ShangMi           http://mirrors.aliyun.com/anolis/8/ShangMi/\$arch/os/
koji add-external-repo -t anolis8-base -m bare anolis8-Experimental      http://mirrors.aliyun.com/anolis/8/Experimental/\$arch/os/

koji add-group anolis8-addons-build build
koji add-group anolis8-addons-build srpm-build

koji add-group-pkg anolis8-addons-build   build  system-rpm-config anolis-release bash bzip2 coreutils cpio diffutils dnf elfutils gcc gcc-c++ gzip make patch python-rpm-macros python3-rpm-macros rpm-build scl-utils-build sed shadow-utils tar unzip util-linux which

koji add-group-pkg anolis8-addons-build   srpm-build   system-rpm-config anolis-release bash bzip2 coreutils cpio diffutils dnf elfutils gcc gcc-c++ gzip make patch python-rpm-macros python3-rpm-macros rpm-build scl-utils-build sed shadow-utils tar unzip util-linux which

koji add-target anolis8-addons anolis8-addons-build anolis8-base-addon-testing




echo "All done!"

exit 0

koji remove-external-repo anolis8-base
