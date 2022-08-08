#!/bin/bash

set -e

deploy()
{
	echo "-----------------------------------------------"
	echo "  deploy $1 $2"
	echo "-----------------------------------------------"
	[ -e $2 ] && rm -rf $2
	mkdir -p `dirname $2` || true
	cp $1 $2 -a
	ls -lh $2
}

# koji cli
deploy cli/koji /usr/bin/koji
deploy cli/koji_cli  /usr/lib/python3.6/site-packages/koji_cli
deploy koji  /usr/lib/python3.6/site-packages/koji
deploy cli/koji.conf /etc/koji.conf 

# koji hub
#/etc/httpd/conf.d/kojihub.conf
#/etc/koji-hub
#/etc/koji-hub/hub.conf
#/etc/koji-hub/hub.conf.d
#/usr/lib/systemd/system/koji-sweep-db.service
#/usr/lib/systemd/system/koji-sweep-db.timer
#/usr/sbin/koji-sweep-db
deploy hub/httpd.conf /etc/httpd/conf.d/kojihub.conf
mkdir -p /etc/koji-hub/hub.conf.d || true
deploy hub/kojixmlrpc.py /usr/share/koji-hub/kojixmlrpc.py

mkdir -p /mnt/koji || true
deploy hub/hub.conf /etc/koji-hub/hub.conf -a



echo "All  done!"
