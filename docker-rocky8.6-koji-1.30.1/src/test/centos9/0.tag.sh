#!/bin/bash

set -x

koji add-tag centos9-base
koji add-tag centos9-base-addon
koji add-tag centos9-base-addon-testing --parent=centos9-base-addon
koji add-tag centos9-addons-build --parent=centos9-base-addon --arches="x86_64"
koji add-tag-inheritance --priority=1 centos9-addons-build centos9-base

#http://mirrors.aliyun.com/centos-stream/9-stream/AppStream/
#http://mirrors.aliyun.com/centos-stream/9-stream/BaseOS/
#http://mirrors.aliyun.com/centos-stream/9-stream/Devel/
#http://mirrors.aliyun.com/centos-stream/9-stream/HighAvailability/
#http://mirrors.aliyun.com/centos-stream/9-stream/PowerTools/
#http://mirrors.aliyun.com/centos-stream/9-stream/centosplus/
#http://mirrors.aliyun.com/centos-stream/9-stream/cloud/
#http://mirrors.aliyun.com/centos-stream/9-stream/configmanagement/
#http://mirrors.aliyun.com/centos-stream/9-stream/cr/
#http://mirrors.aliyun.com/centos-stream/9-stream/extras/
#http://mirrors.aliyun.com/centos-stream/9-stream/fasttrack/
#http://mirrors.aliyun.com/centos-stream/9-stream/infra/
#http://mirrors.aliyun.com/centos-stream/9-stream/kmods/
#http://mirrors.aliyun.com/centos-stream/9-stream/messaging/
#http://mirrors.aliyun.com/centos-stream/9-stream/nfv/
#http://mirrors.aliyun.com/centos-stream/9-stream/opstools/
#http://mirrors.aliyun.com/centos-stream/9-stream/storage/
#http://mirrors.aliyun.com/centos-stream/9-stream/virt/
#
#
#
#
#
#http://mirrors.aliyun.com/centos-stream/9-stream/AppStream/x86_64/os/
#http://mirrors.aliyun.com/centos-stream/9-stream/BaseOS/x86_64/os/
#http://mirrors.aliyun.com/centos-stream/9-stream/Devel/x86_64/os/
#http://mirrors.aliyun.com/centos-stream/9-stream/HighAvailability/x86_64/os/
#http://mirrors.aliyun.com/centos-stream/9-stream/PowerTools/x86_64/os/
#http://mirrors.aliyun.com/centos-stream/9-stream/centosplus/x86_64/os/
#http://mirrors.aliyun.com/centos-stream/9-stream/extras/x86_64/os/

koji add-external-repo -t centos9-base -m bare centos9-AppStream         http://mirrors.aliyun.com/centos-stream/9-stream/AppStream/x86_64/os/
koji add-external-repo -t centos9-base -m bare centos9-BaseOS            http://mirrors.aliyun.com/centos-stream/9-stream/BaseOS/x86_64/os/
koji add-external-repo -t centos9-base -m bare centos9-HighAvailability  http://mirrors.aliyun.com/centos-stream/9-stream/HighAvailability/x86_64/os/
koji add-external-repo -t centos9-base -m bare centos9-ResilientStorage  http://mirrors.aliyun.com/centos-stream/9-stream/ResilientStorage/x86_64/os/

koji add-group centos9-addons-build build
koji add-group centos9-addons-build srpm-build

koji add-group-pkg centos9-addons-build   build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config centos-stream-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz
koji add-group-pkg centos9-addons-build   srpm-build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config centos-stream-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz

koji add-target centos9-addons centos9-addons-build centos9-base-addon-testing


echo "All done!"

exit 0
