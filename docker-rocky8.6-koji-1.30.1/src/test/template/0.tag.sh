#!/bin/bash

set -x

koji add-tag rockylinux8.6-base
koji add-tag rockylinux8.6-base-addon
koji add-tag rockylinux8.6-base-addon-testing --parent=rockylinux8.6-base-addon
koji add-tag rockylinux8.6-addons-build --parent=rockylinux8.6-base-addon --arches="x86_64"
koji add-tag-inheritance --priority=1 rockylinux8.6-addons-build rockylinux8.6-base

koji add-external-repo -t rockylinux8.6-base -m bare rockylinux8.6-AppSteam   http://mirror.nju.edu.cn/rocky/8.6/AppStream/\$arch/os/
koji add-external-repo -t rockylinux8.6-base -m bare rockylinux8.6-BaseOs     http://mirror.nju.edu.cn/rocky/8.6/BaseOS/\$arch/os/
koji add-external-repo -t rockylinux8.6-base -m bare rockylinux8.6-extras     http://mirror.nju.edu.cn/rocky/8.6/extras/\$arch/os/
koji add-external-repo -t rockylinux8.6-base -m bare rockylinux8.6-PowerTools http://mirror.nju.edu.cn/rocky/8.6/PowerTools/\$arch/os/
koji add-external-repo -t rockylinux8.6-base -m bare rockylinux8.6-Devel      http://mirror.nju.edu.cn/rocky/8.6/Devel/\$arch/os/

koji add-group rockylinux8.6-addons-build build
koji add-group rockylinux8.6-addons-build srpm-build

koji add-group-pkg rockylinux8.6-addons-build   build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config rocky-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz ruby fedpkg
koji add-group-pkg rockylinux8.6-addons-build   srpm-build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config rocky-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz ruby fedpkg

koji add-target rockylinux8.6-addons rockylinux8.6-addons-build rockylinux8.6-base-addon-testing




echo "All done!"

exit 0

koji add-external-repo -t rockylinux8.6-base rockylinux8.6-Devel http://mirror.nju.edu.cn/rocky/8.6/Devel/\$arch/os/
koji add-external-repo -t rockylinux8.6-base rockylinux8.6-HighAvailability http://mirror.nju.edu.cn/rocky/8.6/HighAvailability/\$arch/os/


koji add-external-repo -t rockylinux8.6-base rockylinux8.6-baseos http://mirror.nju.edu.cn/rocky/8.6/BaseOS/\$arch/os/
koji add-external-repo -t rockylinux8.6-base rockylinux8.6-powertools http://mirror.nju.edu.cn/rocky/8.6/PowerTools/\$arch/os/
koji add-external-repo -t rockylinux8.6-base rockylinux8.6-appsteam http://mirror.nju.edu.cn/rocky/8.6/AppStream/\$arch/os/
koji add-external-repo -t rockylinux8.6-base rockylinux8.6-devel http://mirror.nju.edu.cn/rocky/8.6/Devel/\$arch/os/
