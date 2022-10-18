#!/bin/bash

set -e

docker container prune -f

docker run --privileged -d -v `pwd`/data:/data -p 8880:8880 -p 8822:22 --name rocky8.6-koji rockylinux8.6-koji /usr/sbin/init

echo "All done!"
