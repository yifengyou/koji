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
* [koji部署](docs/koji部署.md)
* [koji容器化](docs/koji容器化.md)
* [相关技术](docs/相关技术.md)
    * [PostgreSQL](docs/相关技术/PostgreSQL.md)
* [koji源码分析](docs/koji源码分析.md)
    * [koji-hub httpd如何运行koji-hub](docs/koji源码分析/httpd如何运行koji-hub.md)
    * [koji-hub 调试](docs/koji源码分析/调试.md)
    * [koji-hub 连接PostgreSQL](docs/koji源码分析/连接PostgreSQL.md)
    * [koji-cli koji如何通过krb5鉴权](docs/koji源码分析/koji如何通过krb5鉴权.md)
    * [koji-cli 身份认证](docs/koji源码分析/身份认证.md)
* [koji使用](docs/koji使用.md)
    * [koji编译openeuler](docs/koji使用/koji编译openeuler.md)
    * [koji编译rpm基本使用](docs/koji使用/koji编译rpm基本使用.md)




## 图示

![20221005_110039_51](image/20221005_110039_51.png)

![20220811_141522_56](image/20220811_141522_56.png)

![20220811_141624_54](image/20220811_141624_54.png)

![20220811_141636_16](image/20220811_141636_16.png)

![20220811_141746_36](image/20220811_141746_36.png)

![20221018_135919_46](image/20221018_135919_46.png)

---
