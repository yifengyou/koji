# How Fedora's Koji Works

* 国内地址: <https://www.bilibili.com/video/BV1oG4y1V7cQ>
* 国外地址：<https://www.youtube.com/watch?v=hUg6MMC4x0w&ab_channel=Linux.conf.au2011--Brisbane%2CAustralia>

---

![20221126_124101_92](image/20221126_124101_92.png)

![20221126_124110_18](image/20221126_124110_18.png)

![20221126_124122_03](image/20221126_124122_03.png)

![20221126_124130_76](image/20221126_124130_76.png)

![20221126_124252_55](image/20221126_124252_55.png)

![20221126_124347_36](image/20221126_124347_36.png)

**mock + yum + rpmbuild + createrepo**

![20221126_124428_64](image/20221126_124428_64.png)

mock创建chroot环境构建rpm包，独立于当前宿主机环境

![20221126_124552_66](image/20221126_124552_66.png)

yum 用来解析repodata信息，解决依赖安装rpm包

![20221126_124633_52](image/20221126_124633_52.png)

rpmbuild是'导演'，根据'剧本'SPEC演戏

![20221126_124717_85](image/20221126_124717_85.png)

![20221126_124723_77](image/20221126_124723_77.png)

kojihub是rpc server，核心。被动执行，不主动做任何操作

![20221126_124828_36](image/20221126_124828_36.png)

kojira清理仓库

![20221126_124842_11](image/20221126_124842_11.png)

kojid是真正打工人，使用mock/rpmbuild编译包

![20221126_124920_96](image/20221126_124920_96.png)

koji-web，门面，前端界面呈现，但能力有限


![20221126_125010_76](image/20221126_125010_76.png)


常用交互方式就是cli，终端执行

![20221126_125051_47](image/20221126_125051_47.png)


**mash + sigul + bodhi + packagedb**

![20221126_125150_90](image/20221126_125150_90.png)

![20221126_125305_34](image/20221126_125305_34.png)

koji tag 作用？

* tag具有继承性， 不需要每次都scratch

![20221126_125833_48](image/20221126_125833_48.png)

![20221126_125906_47](image/20221126_125906_47.png)

![20221126_125919_81](image/20221126_125919_81.png)


演示：

![20221126_130053_34](image/20221126_130053_34.png)

![20221126_130100_74](image/20221126_130100_74.png)

![20221126_130108_66](image/20221126_130108_66.png)

只有一个可编译的host，几个user， no tag, no targets

![20221126_130120_82](image/20221126_130120_82.png)

setup流程：

![20221126_130501_40](image/20221126_130501_40.png)


```
koji add-tag fedora-14-base
koji add-tag fedora-14-base-addon
koji add-tag fedora-14-base-addon-testing --parent=fedora-14-base-addon
koji add-tag fedora-14-addons-build --parent=fedora-14-addons --arches="i686 x86_64"
koji add-tag-inheritance --priority=1 fedora-14-addons-build fedora-14-base

koji add-external-repo -t fedora-14-base fedora-14 http://192.169.122.60/Fedora/\$arch/os/


koji add-group fedora-14-addons-build build
koji add-group-pkg fedora-14-addons-build build bash bzip2 coreutils cpio diffutils fedora-release findutils gawk gcc gcc-c++ grep gzip info make patch redhat-rpm-config rpm-build sed shadow-utils tar unzip util-linux-ng which xz
koji list-groups fedora-14-addons-build


koji add-target fedora-14-addons fedora-14-addons-build fedora-14-addons-testing
koji add-pkg --owner=admin fedora-14-addons bash binutils


```

![20221126_130831_26](image/20221126_130831_26.png)

![20221126_130841_10](image/20221126_130841_10.png)


![20221126_131529_66](image/20221126_131529_66.png)

![20221126_131728_24](image/20221126_131728_24.png)

![20221126_131743_97](image/20221126_131743_97.png)

![20221126_132023_72](image/20221126_132023_72.png)

![20221126_132224_83](image/20221126_132224_83.png)



![20221126_132306_36](image/20221126_132306_36.png)

![20221126_132343_59](image/20221126_132343_59.png)

![20221126_132508_29](image/20221126_132508_29.png)

![20221126_132518_80](image/20221126_132518_80.png)

![20221126_132531_28](image/20221126_132531_28.png)


![20221126_132559_82](image/20221126_132559_82.png)

![20221126_132610_35](image/20221126_132610_35.png)

![20221126_132956_16](image/20221126_132956_16.png)

![20221126_133020_85](image/20221126_133020_85.png)

```
koji build fedora-14-addons bash-4.1.7-3.fc14.src.rpm
```

![20221126_133125_61](image/20221126_133125_61.png)


![20221126_133147_76](image/20221126_133147_76.png)

![20221126_133505_19](image/20221126_133505_19.png)

![20221126_133519_78](image/20221126_133519_78.png)

![20221126_133934_51](image/20221126_133934_51.png)

![20221126_134432_32](image/20221126_134432_32.png)

![20221126_134450_76](image/20221126_134450_76.png)








---
