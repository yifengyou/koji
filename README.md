# Rocky Linux koji-1.29.1


![20220806_231000_79](image/20220806_231000_79.png)

```
Something I hope you know before go into the coding~
First, please watch or star this repo, I'll be more happy if you follow me.
Bug report, questions and discussion are welcome, you can post an issue or pull a request.
```

## 简介

```
Koji is an RPM-based build system. The Fedora Project uses Koji for their build system, as do several other projects.

Koji's goal is to provide a flexible, secure, and reproducible way to build software.
```

* New buildroot for each build
* Robust XML-RPC APIs for easy integration with other tools
* Web interface with SSL and Kerberos authentication
* Thin, portable command line client
* Users can create local buildroots
* Buildroot contents are tracked in the database
* Versioned data

相关站点：

* <https://pagure.io/koji/>
* <https://docs.pagure.org/koji/>


## koji入门到入土必备技能

1. Python
2. kerberos
3. PostgreSQL
4. rpmbuild/mock



## 目录

* [koji玩耍指南](docs/koji玩耍指南.md)
    * [知己知彼](docs/koji玩耍指南/知己知彼.md)
    * [帮助信息](docs/koji玩耍指南/帮助信息.md)
    * [玩起来](docs/koji玩耍指南/玩起来.md)
    * [入口解析](docs/koji玩耍指南/入口解析.md)
    * [调试](docs/koji玩耍指南/调试.md)
    * [koji如何通过krb5鉴权](docs/koji玩耍指南/koji如何通过krb5鉴权.md)
    * [ssl证书生成](docs/koji玩耍指南/ssl证书生成.md)
    * [PostgreSQL入门到入土](docs/koji玩耍指南/PostgreSQL入门到入土.md)
    * [kojihub如何连接PostgreSQL](docs/koji玩耍指南/kojihub如何连接PostgreSQL.md)
    * [koji身份认证](docs/koji玩耍指南/koji身份认证.md)
    * [koji编译rpm基本使用](docs/koji玩耍指南/koji编译rpm基本使用.md)


## 图示

![20221005_110039_51](image/20221005_110039_51.png) 


![20220811_141522_56](image/20220811_141522_56.png)

![20220811_141624_54](image/20220811_141624_54.png)

![20220811_141636_16](image/20220811_141636_16.png)

![20220811_141746_36](image/20220811_141746_36.png)





























---
