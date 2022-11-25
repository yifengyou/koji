# 知己知彼


* <https://blog.csdn.net/leapmotion/article/details/115433407>
* <https://fedoraproject.org/wiki/Zh/%E6%9E%84%E5%BB%BAKoji%E7%BC%96%E8%AF%91%E6%9C%8D%E5%8A%A1%E5%99%A8>

![20220808_095351_37](image/20220808_095351_37.png)


```
[root@ctyun-rocky ~]# rpm -qa|grep koji
koji-hub-1.29.1-1.el8.noarch
python3-koji-1.29.1-1.el8.noarch
python3-koji-web-1.29.1-1.el8.noarch
koji-web-1.29.1-1.el8.noarch
python3-koji-hub-1.29.1-1.el8.noarch
koji-builder-1.29.1-1.el8.noarch
koji-1.29.1-1.el8.noarch
```


```
koji.noarch : Build system tools
koji-builder.noarch : Koji RPM builder daemon
koji-builder-plugins.noarch : Koji builder plugins
koji-hub.noarch : Koji XMLRPC interface
koji-hub-plugins.noarch : Koji hub plugins
koji-utils.noarch : Koji Utilities
koji-vm.noarch : Koji virtual machine management daemon
koji-web.noarch : Koji Web UI
python3-koji.noarch : Build system tools python library
python3-koji-cli-plugins.noarch : Koji client plugins
python3-koji-hub.noarch : Koji XMLRPC interface
python3-koji-hub-plugins.noarch : Koji hub plugins
python3-koji-web.noarch : Koji Web UI
supybot-koji.noarch : Plugin for Supybot to interact with Koji instances
```



![20221125_142300_83](image/20221125_142300_83.png)




## 代码量

移除test目录，还有大概3.5W行的python代码

![20221125_153443_27](image/20221125_153443_27.png)


![20221125_153532_20](image/20221125_153532_20.png)

测试代码比工程代码多，是个练家子







---
