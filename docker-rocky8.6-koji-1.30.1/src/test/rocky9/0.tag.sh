#!/bin/bash

set -x

koji add-tag rockylinux9-base
koji add-tag rockylinux9-base-addon
koji add-tag rockylinux9-base-addon-testing --parent=rockylinux9-base-addon
koji add-tag rockylinux9-addons-build --parent=rockylinux9-base-addon --arches="x86_64"
koji add-tag-inheritance --priority=1 rockylinux9-addons-build rockylinux9-base

koji add-external-repo -t rockylinux9-base -m bare rockylinux9-AppSteam   http://mirror.nju.edu.cn/rocky/9/AppStream/\$arch/os/
koji add-external-repo -t rockylinux9-base -m bare rockylinux9-BaseOs     http://mirror.nju.edu.cn/rocky/9/BaseOS/\$arch/os/
koji add-external-repo -t rockylinux9-base -m bare rockylinux9-extras     http://mirror.nju.edu.cn/rocky/9/extras/\$arch/os/
koji add-external-repo -t rockylinux9-base -m bare rockylinux9-PowerTools http://mirror.nju.edu.cn/rocky/9/PowerTools/\$arch/os/
koji add-external-repo -t rockylinux9-base -m bare rockylinux9-Devel      http://mirror.nju.edu.cn/rocky/9/Devel/\$arch/os/

koji add-group rockylinux9-addons-build build
koji add-group rockylinux9-addons-build srpm-build

koji add-group-pkg rockylinux9-addons-build   build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config rocky-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz ruby fedpkg
koji add-group-pkg rockylinux9-addons-build   srpm-build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config rocky-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz ruby fedpkg

koji add-target rockylinux9-addons rockylinux9-addons-build rockylinux9-base-addon-testing




echo "All done!"

exit 0

koji add-external-repo -t rockylinux9-base rockylinux9-Devel http://mirror.nju.edu.cn/rocky/9/Devel/\$arch/os/
koji add-external-repo -t rockylinux9-base rockylinux9-HighAvailability http://mirror.nju.edu.cn/rocky/9/HighAvailability/\$arch/os/


koji add-external-repo -t rockylinux9-base rockylinux9-baseos http://mirror.nju.edu.cn/rocky/9/BaseOS/\$arch/os/
koji add-external-repo -t rockylinux9-base rockylinux9-powertools http://mirror.nju.edu.cn/rocky/9/PowerTools/\$arch/os/
koji add-external-repo -t rockylinux9-base rockylinux9-appsteam http://mirror.nju.edu.cn/rocky/9/AppStream/\$arch/os/
koji add-external-repo -t rockylinux9-base rockylinux9-devel http://mirror.nju.edu.cn/rocky/9/Devel/\$arch/os/
