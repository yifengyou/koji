#!/bin/bash

set -e

#cp /etc/httpd/conf.d /etc/httpd/conf.d.bak -a

mkdir -p /mnt/koji || true
cd /mnt/koji
mkdir {packages,repos,work,scratch} || true
chown -R apache.apache *
systemctl start httpd
systemctl status httpd --no-pager

echo "All done!"
