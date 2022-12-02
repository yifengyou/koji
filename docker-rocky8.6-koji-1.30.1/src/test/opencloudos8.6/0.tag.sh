#!/bin/bash

set -x

koji add-tag opencloudos8.6-base
koji add-tag opencloudos8.6-base-addon
koji add-tag opencloudos8.6-base-addon-testing --parent=opencloudos8.6-base-addon
koji add-tag opencloudos8.6-addons-build --parent=opencloudos8.6-base-addon --arches="x86_64"
koji add-tag-inheritance --priority=1 opencloudos8.6-addons-build opencloudos8.6-base

#http://mirrors.tencent.com/opencloudos/8.6/AppStream/x86_64/os/
#http://mirrors.tencent.com/opencloudos/8.6/BaseOS/x86_64/os/
#http://mirrors.tencent.com/opencloudos/8.6/Extras/x86_64/os/
#http://mirrors.tencent.com/opencloudos/8.6/HighAvailability/x86_64/os/
#http://mirrors.tencent.com/opencloudos/8.6/PowerTools/x86_64/os/
#http://mirrors.tencent.com/opencloudos/8.6/ResilientStorage/x86_64/os/
#http://mirrors.tencent.com/opencloudos/8.6/Updates/x86_64/os/
#http://mirrors.tencent.com/opencloudos/8.6/extras/x86_64/os/


koji add-external-repo -t opencloudos8.6-base -m bare opencloudos8.6-AppSteam             http://mirrors.tencent.com/opencloudos/8.6/AppStream/x86_64/os/
koji add-external-repo -t opencloudos8.6-base -m bare opencloudos8.6-BaseOs               http://mirrors.tencent.com/opencloudos/8.6/BaseOS/x86_64/os/
koji add-external-repo -t opencloudos8.6-base -m bare opencloudos8.6-Extras               http://mirrors.tencent.com/opencloudos/8.6/Extras/x86_64/os/
koji add-external-repo -t opencloudos8.6-base -m bare opencloudos8.6-HighAvailability     http://mirrors.tencent.com/opencloudos/8.6/HighAvailability/x86_64/os/
koji add-external-repo -t opencloudos8.6-base -m bare opencloudos8.6-PowerTools           http://mirrors.tencent.com/opencloudos/8.6/PowerTools/x86_64/os/
koji add-external-repo -t opencloudos8.6-base -m bare opencloudos8.6-ResilientStorage     http://mirrors.tencent.com/opencloudos/8.6/ResilientStorage/x86_64/os/
koji add-external-repo -t opencloudos8.6-base -m bare opencloudos8.6-Updates              http://mirrors.tencent.com/opencloudos/8.6/Updates/x86_64/os/
koji add-external-repo -t opencloudos8.6-base -m bare opencloudos8.6-extras               http://mirrors.tencent.com/opencloudos/8.6/extras/x86_64/os/

koji add-group opencloudos8.6-addons-build build
koji add-group opencloudos8.6-addons-build srpm-build

koji add-group-pkg opencloudos8.6-addons-build   build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config opencloudos-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz ruby fedpkg
koji add-group-pkg opencloudos8.6-addons-build   srpm-build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config opencloudos-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz ruby fedpkg

koji add-target opencloudos8.6-addons opencloudos8.6-addons-build opencloudos8.6-base-addon-testing


echo "All done!"

exit 0

#http://mirrors.tencent.com/opencloudos/8.6/AppStream/
#http://mirrors.tencent.com/opencloudos/8.6/BaseOS/
#http://mirrors.tencent.com/opencloudos/8.6/Extras/
#http://mirrors.tencent.com/opencloudos/8.6/HighAvailability/
#http://mirrors.tencent.com/opencloudos/8.6/Minimal/
#http://mirrors.tencent.com/opencloudos/8.6/PowerTools/
#http://mirrors.tencent.com/opencloudos/8.6/ResilientStorage/
#http://mirrors.tencent.com/opencloudos/8.6/Updates/
#http://mirrors.tencent.com/opencloudos/8.6/extras/
#http://mirrors.tencent.com/opencloudos/8.6/kernel-ocks/
#
#
#http://mirrors.tencent.com/opencloudos/8.6/AppStream/x86_64/os/
#http://mirrors.tencent.com/opencloudos/8.6/BaseOS/x86_64/os/
#http://mirrors.tencent.com/opencloudos/8.6/Extras/x86_64/os/
#http://mirrors.tencent.com/opencloudos/8.6/HighAvailability/x86_64/os/
#http://mirrors.tencent.com/opencloudos/8.6/PowerTools/x86_64/os/
#http://mirrors.tencent.com/opencloudos/8.6/ResilientStorage/x86_64/os/
#http://mirrors.tencent.com/opencloudos/8.6/Updates/x86_64/os/
#http://mirrors.tencent.com/opencloudos/8.6/extras/x86_64/os/