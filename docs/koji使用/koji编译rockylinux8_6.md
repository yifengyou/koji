# koji编译rockylinux8.6




```
koji add-tag rockylinux8.6-base
koji add-tag rockylinux8.6-base-addon
koji add-tag rockylinux8.6-base-addon-testing --parent=rockylinux8.6-base-addon
koji add-tag rockylinux8.6-addons-build --parent=rockylinux8.6-base-addon --arches="x86_64"
koji add-tag-inheritance --priority=1 rockylinux8.6-addons-build rockylinux8.6-base

koji add-external-repo -t rockylinux8.6-base rockylinux8.6-baseos http://mirror.nju.edu.cn/rocky/8.6/BaseOS/\$arch/os/
koji add-external-repo -t rockylinux8.6-base rockylinux8.6-devel http://mirror.nju.edu.cn/rocky/8.6/Devel/\$arch/os/
koji add-external-repo -t rockylinux8.6-base rockylinux8.6-powertools http://mirror.nju.edu.cn/rocky/8.6/PowerTools/\$arch/os/
koji add-external-repo -t rockylinux8.6-base rockylinux8.6-appsteam http://mirror.nju.edu.cn/rocky/8.6/AppStream/\$arch/os/

koji add-group rockylinux8.6-addons-build build
koji add-group rockylinux8.6-addons-build srpm-build

koji add-group-pkg rockylinux8.6-addons-build   build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config rocky-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz ruby curl passwd
koji add-group-pkg rockylinux8.6-addons-build   srpm-build    bash bzip2 coreutils cpio diffutils findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config rocky-release rpm-build sed shadow-utils tar unzip util-linux which xz rpmdevtools  which xz ruby curl passwd

koji add-target rockylinux8.6-addons rockylinux8.6-addons-build rockylinux8.6-base-addon-testing












koji build rockylinux8.6-addons curl-7.61.1-25.el8.src.rpm
```





koji add-group rockylinux8.6-addons-build build
koji add-group-pkg rockylinux8.6-addons-build build bash tar gcc-c++ redhat-rpm-config which xz sed make bzip2 gzip gcc coreutils unzip shadow-utils diffutils cpio bash gawk rpm-build info patch util-linux findutils grep  rocky-release rpm-build
koji list-groups rockylinux8.6-addons-build










koji add-external-repo -t rockylinux8.6-base rockylinux8.6-devel http://mirror.nju.edu.cn/rocky/8.6/Devel/\$arch/os/
koji add-external-repo -t rockylinux8.6-base rockylinux8.6-powertools http://mirror.nju.edu.cn/rocky/8.6/PowerTools/\$arch/os/
koji add-external-repo -t rockylinux8.6-base rockylinux8.6-appsteam http://mirror.nju.edu.cn/rocky/8.6/AppStream/\$arch/os/

```
koji add-pkg --owner=kojiadmin rockylinux8.6-addons bash binutils
```

![20221126_181531_66](image/20221126_181531_66.png)

![20221126_182057_57](image/20221126_182057_57.png)





koji add-group-pkg rockylinux8.6-addons-build build bash bzip2 coreutils cpio diffutils fedora-release findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config rpm-build sed shadow-utils tar unzip util-linux-ng which xz




koji add-group-pkg rockylinux8.6-addons-build build bash tar gcc-c++ redhat-rpm-config redhat-release which xz sed make bzip2 gzip gcc coreutils unzip shadow-utils diffutils cpio bash gawk rpm-build info patch util-linux findutils grep  rocky-release rpm-build


## rocky linux源码仓库结构

![20221127_213409_72](image/20221127_213409_72.png)

* <https://wiki.rockylinux.org/special_interest_groups/sig_guide/content/#importing-to-the-rocky-linux-gitlab>


* <https://docs.rockylinux.org/guides/package_management/developer_start2/#4-use-rocky-devtools-rockybuild-to-build-a-new-package-for-the-rocky-os>

rockylinux 工具集




---
