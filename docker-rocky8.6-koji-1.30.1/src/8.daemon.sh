#!/bin/bash

set -e

docker container prune -f

[ ! -d koji-data ] && mkdir koji-data

docker run \
	--privileged -d \
	-v `pwd`/test:/test \
	-v `pwd`/koji-data:/data \
	-p 9980:80 \
	-p 5432:5432 \
	--name rocky8.6-koji \
	rockylinux8.6-koji \
	/usr/sbin/init

echo "All done!"
