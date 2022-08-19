#!/bin/bash

set -xe

# koji cli
cp -a cli/koji /usr/bin/koji
cp -a cli/koji.conf /etc/koji.conf 

rm -rf /usr/lib/python3.6/site-packages/koji_cli
cp -a cli/koji_cli  /usr/lib/python3.6/site-packages/

rm -rf  /usr/lib/python3.6/site-packages/koji/
cp -a koji  /usr/lib/python3.6/site-packages/

# koji hub
#/etc/httpd/conf.d/kojihub.conf
#/etc/koji-hub
#/etc/koji-hub/hub.conf
#/etc/koji-hub/hub.conf.d
#/usr/lib/systemd/system/koji-sweep-db.service
#/usr/lib/systemd/system/koji-sweep-db.timer
#/usr/sbin/koji-sweep-db

cp -a hub/httpd.conf /etc/httpd/conf.d/kojihub.conf
mkdir -p /etc/koji-hub/hub.conf.d || true
cp -a hub/kojixmlrpc.py /usr/share/koji-hub/kojixmlrpc.py
cp -a hub/kojihub.py /usr/share/koji-hub/kojihub.py
cp -a hub/__init__.py /usr/share/koji-hub/__init__.py

mkdir -p /mnt/koji || true
cp -a hub/hub.conf /etc/koji-hub/hub.conf -a
systemctl daemon-reload

# kojira
mkdir /etc/kojira || true
cp -a util/kojira.conf /etc/kojira/kojira.conf
cp -a util/kojira /usr/sbin/kojira
chmod +x /usr/sbin/kojira
cp -a util/kojira.service /usr/lib/systemd/system/kojira.service
systemctl daemon-reload
#systemctl restart kojira


# kojid
cp -a builder/kojid /usr/sbin/kojid
chmod +x /usr/sbin/kojid
mkdir /etc/kojid || true
cp -a builder/kojid.conf /etc/kojid/kojid.conf
cp -a builder/kojid.service /usr/lib/systemd/system/kojid.service
systemctl daemon-reload
#systemctl restart kojid


# kojiweb
mkdir /etc/kojiweb || true
cp www/conf/web.conf  /etc/kojiweb/web.conf
mkdir -p /etc/httpd/conf.d/ || true
mkdir -p /etc/kojiweb/web.conf.d/ || true
cp www/conf/kojiweb.conf /etc/httpd/conf.d/kojiweb.conf

rm -rf /usr/share/koji-web || true
mkdir /usr/share/koji-web -p || true

cp -a www/kojiweb /usr/share/koji-web/scripts
cp -a www/lib /usr/share/koji-web/lib
cp -a www/static /usr/share/koji-web/static

systemctl restart httpd



echo "All  done!"

