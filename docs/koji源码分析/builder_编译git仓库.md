<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:1 updateOnSave:1 -->

- [kojid 编译git仓库](#kojid-编译git仓库)   
   - [错误处理: Could not find the fragment element](#错误处理-could-not-find-the-fragment-element)   
   - [错误: No rule to make target 'sources'.  Stop.](#错误-no-rule-to-make-target-sources-stop)   

<!-- /MDTOC -->

# kojid 编译git仓库








## 错误处理: Could not find the fragment element

![20221127_083611_39](image/20221127_083611_39.png)

位置很明确

![20221127_084418_60](image/20221127_084418_60.png)

![20221127_084557_66](image/20221127_084557_66.png)


这里urllib.parse.urlparse

![20221127_103224_56](image/20221127_103224_56.png)



git+https://git.rockylinux.org/staging/src/rocky-release

```
scheme://netloc/path;parameters?query#fragment
```

* <https://www.bilibili.com/read/cv15032641>

![20221127_103448_82](image/20221127_103448_82.png)





![20221127_103618_39](image/20221127_103618_39.png)

```
#koji build [tag] [scheme]://[user]@[hostname]/[path/to/repository]?[path/to/project]#[revision]
```

* <https://fedoraproject.org/wiki/Koji/KojiMisc>

```
git+https://git.rockylinux.org/staging/src/rocky-release?staging/src/rocky-release#r8
```

支持这几种scm同步

![20221127_111644_42](image/20221127_111644_42.png)


哪里来的common ?
![20221127_112355_64](image/20221127_112355_64.png)

![20221127_112417_40](image/20221127_112417_40.png)


![20221127_113428_88](image/20221127_113428_88.png)

![20221127_113449_18](image/20221127_113449_18.png)

修改配置，添加":no" 即可

![20221127_113517_34](image/20221127_113517_34.png)

checkout就正常了

总结：git链接参数不对


## 错误: No rule to make target 'sources'.  Stop.

![20221127_114104_29](image/20221127_114104_29.png)

![20221127_114131_37](image/20221127_114131_37.png)

定位源码

![20221127_114246_11](image/20221127_114246_11.png)

难道一定要有Makefile文件，一定要有sources目标？

![20221127_114334_34](image/20221127_114334_34.png)

应该可以设置

![20221127_114601_48](image/20221127_114601_48.png)


![20221127_114729_50](image/20221127_114729_50.png)

* <https://docs.pagure.org/koji/kojid_conf/>


![20221127_114814_84](image/20221127_114814_84.png)

这里文档很明确

![20221127_115428_39](image/20221127_115428_39.png)


![20221127_115933_26](image/20221127_115933_26.png)

可以用fedpkg sources

```
allowed_scms=git.rockylinux.org:/*:no:fedpkg,sources


allowed_scms=git.rockylinux.org:/*:no:fedpkg,sources git.centos.org:/*:no git.rockylinux.org:/*:no gitee.com:/*:no github.com:/*:no

```

![20221127_130510_56](image/20221127_130510_56.png)

rocky用的是 ```/var/srpmproc/srpmproc_wrapper```

看起来像 ```https://github.com/rocky-linux/srpmproc```

```
---
# vars for kojid

kojid_vendor: Rocky
kojid_packager: infrastructure@rockylinux.org
kojid_distribution: Rocky
# These three should probably be specified by special vars
# kojid_web_url: https://koji.rockylinux.org/koji
# kojid_hub_url: https://koji.rockylinux.org/kojihub
# kojid_files_url: https://koji.rockylinux.org/kojifiles

kojid_ca_bundle: /etc/pki/tls/certs/ca-bundle.crt
kojid_keytab: /etc/kojid.keytab
kojid_smtp_host: smtp.rockylinux.org
kojid_allowed_scm: "git.rockylinux.org:/staging/rpms/*:off:/var/srpmproc/srpmproc_wrapper git.rockylinux.org:/rocky/*:off:/var/srpmproc/srpmproc_wrapper git.rockylinux.org:/original/rpms/*:off:/var/srpmproc/srpmproc_wrapper"
...
```

* <https://github.com/rocky-linux/wiki.rockylinux.org/blob/d9577615315996e588379123018a2b03b5a53ee4/docs/archive/legacy/koji_setup.md>

![20221127_131345_54](image/20221127_131345_54.png)


总结：

源码包->srcrpm的过程

对于centos，scm-> srpm有工具	```get_sources.sh```

<https://git.centos.org/centos-git-common/tree/master>

```
git clone https://git.centos.org/centos-git-common
cp centos-git-common/* /bin/ -a
chmod +x /bin/get_sources.sh

git clone https://git.centos.org/rpms/acpid
cd acpid
git checkout c8
get_sources.sh
```

![20221127_132824_19](image/20221127_132824_19.png)

这个操作，其实是获取源代码而已，不是构建srcrpm包



对于rockylinux,


![20221127_140913_19](image/20221127_140913_19.png) 









---
