#!/bin/bash

set -x

koji add-tag centos8-base
koji add-tag centos8-base-addon
koji add-tag centos8-base-addon-testing --parent=centos8-base-addon
koji add-tag centos8-addons-build --parent=centos8-base-addon --arches="x86_64"
koji add-tag-inheritance --priority=1 centos8-addons-build centos8-base

#http://mirrors.aliyun.com/centos/8/AppStream/
#http://mirrors.aliyun.com/centos/8/BaseOS/
#http://mirrors.aliyun.com/centos/8/Devel/
#http://mirrors.aliyun.com/centos/8/HighAvailability/
#http://mirrors.aliyun.com/centos/8/PowerTools/
#http://mirrors.aliyun.com/centos/8/centosplus/
#http://mirrors.aliyun.com/centos/8/cloud/
#http://mirrors.aliyun.com/centos/8/configmanagement/
#http://mirrors.aliyun.com/centos/8/cr/
#http://mirrors.aliyun.com/centos/8/extras/
#http://mirrors.aliyun.com/centos/8/fasttrack/
#http://mirrors.aliyun.com/centos/8/infra/
#http://mirrors.aliyun.com/centos/8/kmods/
#http://mirrors.aliyun.com/centos/8/messaging/
#http://mirrors.aliyun.com/centos/8/nfv/
#http://mirrors.aliyun.com/centos/8/opstools/
#http://mirrors.aliyun.com/centos/8/storage/
#http://mirrors.aliyun.com/centos/8/virt/
#
#
#
#
#
#http://mirrors.aliyun.com/centos/8/AppStream/x86_64/os/
#http://mirrors.aliyun.com/centos/8/BaseOS/x86_64/os/
#http://mirrors.aliyun.com/centos/8/Devel/x86_64/os/
#http://mirrors.aliyun.com/centos/8/HighAvailability/x86_64/os/
#http://mirrors.aliyun.com/centos/8/PowerTools/x86_64/os/
#http://mirrors.aliyun.com/centos/8/centosplus/x86_64/os/
#http://mirrors.aliyun.com/centos/8/extras/x86_64/os/

koji add-external-repo -t centos8-base -m bare centos8-AppStream         http://mirrors.aliyun.com/centos/8/AppStream/x86_64/os/
koji add-external-repo -t centos8-base -m bare centos8-BaseOS            http://mirrors.aliyun.com/centos/8/BaseOS/x86_64/os/
koji add-external-repo -t centos8-base -m bare centos8-Devel             http://mirrors.aliyun.com/centos/8/Devel/x86_64/os/
koji add-external-repo -t centos8-base -m bare centos8-HighAvailability  http://mirrors.aliyun.com/centos/8/HighAvailability/x86_64/os/
koji add-external-repo -t centos8-base -m bare centos8-PowerTools        http://mirrors.aliyun.com/centos/8/PowerTools/x86_64/os/
koji add-external-repo -t centos8-base -m bare centos8-centosplus        http://mirrors.aliyun.com/centos/8/centosplus/x86_64/os/
koji add-external-repo -t centos8-base -m bare centos8-extras            http://mirrors.aliyun.com/centos/8/extras/x86_64/os/

koji add-group centos8-addons-build build
koji add-group centos8-addons-build srpm-build

koji add-group-pkg centos8-addons-build   build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config centos-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz ruby fedpkg
koji add-group-pkg centos8-addons-build   srpm-build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config centos-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz ruby fedpkg

koji add-target centos8-addons centos8-addons-build centos8-base-addon-testing


echo "All done!"

exit 0
