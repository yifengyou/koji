#!/bin/bash

set -x

koji add-tag centos7-base
koji add-tag centos7-base-addon
koji add-tag centos7-base-addon-testing --parent=centos7-base-addon
koji add-tag centos7-addons-build --parent=centos7-base-addon --arches="x86_64"
koji add-tag-inheritance --priority=1 centos7-addons-build centos7-base

#https://mirrors.aliyun.com/centos/7/atomic
#https://mirrors.aliyun.com/centos/7/centosplus
#https://mirrors.aliyun.com/centos/7/cloud
#https://mirrors.aliyun.com/centos/7/configmanagement
#https://mirrors.aliyun.com/centos/7/cr
#https://mirrors.aliyun.com/centos/7/dotnet
#https://mirrors.aliyun.com/centos/7/extras
#https://mirrors.aliyun.com/centos/7/fasttrack
#https://mirrors.aliyun.com/centos/7/infra
#https://mirrors.aliyun.com/centos/7/isos
#https://mirrors.aliyun.com/centos/7/messaging
#https://mirrors.aliyun.com/centos/7/nfv/
#https://mirrors.aliyun.com/centos/7/opstools/
#https://mirrors.aliyun.com/centos/7/os/
#https://mirrors.aliyun.com/centos/7/paas/
#https://mirrors.aliyun.com/centos/7/rt/
#https://mirrors.aliyun.com/centos/7/sclo/
#https://mirrors.aliyun.com/centos/7/storage/
#https://mirrors.aliyun.com/centos/7/updates/
#https://mirrors.aliyun.com/centos/7/virt/


#https://mirrors.aliyun.com/centos/7/os/
#https://mirrors.aliyun.com/centos/7/updates/
#https://mirrors.aliyun.com/centos/7/extras
#https://mirrors.aliyun.com/centos/7/centosplus

koji add-external-repo -t centos7-base -m bare centos7-os   https://mirrors.aliyun.com/centos/7/os/x86_64/
koji add-external-repo -t centos7-base -m bare centos7-updates     https://mirrors.aliyun.com/centos/7/updates/x86_64/
koji add-external-repo -t centos7-base -m bare centos7-extras     https://mirrors.aliyun.com/centos/7/extras/x86_64/
koji add-external-repo -t centos7-base -m bare centos7-centosplus https://mirrors.aliyun.com/centos/7/centosplus/x86_64/

koji add-group centos7-addons-build build
koji add-group centos7-addons-build srpm-build

koji add-group-pkg centos7-addons-build   build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config centos-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz ruby fedpkg
koji add-group-pkg centos7-addons-build   srpm-build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config centos-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz ruby fedpkg

koji add-target centos7-addons centos7-addons-build centos7-base-addon-testing


echo "All done!"

exit 0
