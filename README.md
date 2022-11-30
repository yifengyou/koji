# koji解析

```
Something I hope you know before go into the coding~
First, please watch or star this repo, I'll be more happy if you follow me.
Bug report, questions and discussion are welcome, you can post an issue or pull a request.
```

![20220806_231000_79](image/20220806_231000_79.png)

Koji is an RPM-based build system. The Fedora Project uses Koji for their build system, as do several other projects.

Koji's goal is to provide a flexible, secure, and reproducible way to build software.


* New buildroot for each build
* Robust XML-RPC APIs for easy integration with other tools
* Web interface with SSL and Kerberos authentication
* Thin, portable command line client
* Users can create local buildroots
* Buildroot contents are tracked in the database
* Versioned data

## 相关站点

* 官方源码：<https://pagure.io/koji>
* 官方文档：<https://docs.pagure.org/koji/>
* Fedora官方koji站点：<https://koji.fedoraproject.org/koji/>
* CentOS官方koji站点：<https://cbs.centos.org/koji/>
* RockyLinux官方koji站点：<https://koji.rockylinux.org/koji/>

## 目录


* [koji介绍](docs/koji介绍.md)
* [koji站点汇总](docs/koji站点汇总.md)
* [koji部署](docs/koji部署.md)
* [koji容器化](docs/koji容器化.md)
* [koji核心概念](docs/koji核心概念.md)
* [相关技术](docs/相关技术.md)
    * [PostgreSQL](docs/相关技术/PostgreSQL.md)
    * [kerberos](docs/相关技术/kerberos.md)
    * [psycopg2](docs/相关技术/psycopg2.md)
* [koji源码分析](docs/koji源码分析.md)
    * [koji-hub httpd如何运行koji-hub](docs/koji源码分析/httpd如何运行koji-hub.md)
    * [koji-hub 入口程序application](docs/koji源码分析/入口程序application.md)
    * [koji-hub curl发送调试请求](docs/koji源码分析/curl发送调试请求.md)
    * [koji-hub 获取路由列表](docs/koji源码分析/获取路由列表.md)
    * [koji-hub 连接PostgreSQL](docs/koji源码分析/连接PostgreSQL.md)
    * [koji-hub SQL表拆解](docs/koji源码分析/SQL表拆解.md)
    * [kojid builder入口解析](docs/koji源码分析/builder入口解析.md)
    * [kojid builder如何与koji-hub交互](docs/koji源码分析/builder如何与koji-hub交互.md)
    * [kojid smtp发送邮件](docs/koji源码分析/builder_smtp发送邮件.md)
    * [kojid 编译git仓库](docs/koji源码分析/builder_编译git仓库.md)
    * [koji-cli koji如何通过krb5鉴权](docs/koji源码分析/koji如何通过krb5鉴权.md)
    * [koji-cli 身份认证](docs/koji源码分析/身份认证.md)
    * [koji-cli watch-task使用及解析](docs/koji源码分析/watch-task使用及解析.md)
    * [mock中使用systemd-nspawn](docs/koji源码分析/mock中使用systemd-nspawn.md)
    * [koji task执行后notifications使用及解析](docs/koji源码分析/task执行后notifications使用及解析.md)
* [koji使用](docs/koji使用.md)
    * [koji编译centos7](docs/koji使用/koji编译centos7.md)
    * [koji编译rockylinux8.6](docs/koji使用/koji编译rockylinux8_6.md)
    * [koji编译openeuler](docs/koji使用/koji编译openeuler.md)
    * [koji编译anolis](docs/koji使用/koji编译anolis.md)
* [公开课](docs/公开课.md)
    * [How Fedora's Koji Works](docs/公开课/How_Fedoras_Koji_Works.md)
    * [Building RPMs with Gitlab and Koji](docs/公开课/Building_RPMs_with_Gitlab_and_Koji.md)
    * [Intro to Koji Build System](docs/公开课/Intro_to_Koji_Build_System.md)
    * [CentOS Buildsystems and infrastructure](docs/公开课/CentOS_Buildsystems_and_infrastructure.md)



## 图示

![20221005_110039_51](image/20221005_110039_51.png)

![20220811_141522_56](image/20220811_141522_56.png)

![20220811_141624_54](image/20220811_141624_54.png)

![20220811_141636_16](image/20220811_141636_16.png)

![20220811_141746_36](image/20220811_141746_36.png)

![20221018_135919_46](image/20221018_135919_46.png)
















---
