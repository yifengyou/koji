#!/bin/bash

docker run -d --privileged --name rocky-koji -v /data/:/data -v /root/rpmbuild:/root/rpmbuild rockylinux:8.6 /sbin/init
