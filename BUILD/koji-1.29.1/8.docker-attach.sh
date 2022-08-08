#!/bin/bash


docker exec -it rocky-koji /bin/bash


exit 0
docker run -d --privileged --name rocky-koji -v /data/:/data -v /root/rpmbuild:/root/rpmbuild rockylinux:8.6 /sbin/init
