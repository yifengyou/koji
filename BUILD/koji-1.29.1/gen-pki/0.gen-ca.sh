#!/bin/bash

set -xe

WORKDIR=`pwd`

cat > /etc/selinux/config << EOF
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX=disabled
# SELINUXTYPE= can take one of these three values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are protected. 
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted

EOF

if [ -d /etc/pki/koji ]
then
	mv /etc/pki/koji /etc/pki/koji-$RANDOM
fi

mkdir /etc/pki/koji
cp -a ${WORKDIR}/ssl.cnf /etc/pki/koji/

cd /etc/pki/koji/
mkdir {certs,private} 
touch index.txt
echo 01 > serial

export caname=koji
openssl genrsa -out private/${caname}_ca_cert.key 2048

openssl rand -writerand .rand

ls -alh .rand

openssl req \
	-config ssl.cnf \
	-new -x509 -days 3650 \
	-key private/${caname}_ca_cert.key \
	-out ${caname}_ca_cert.crt \
	-extensions v3_ca \
	-subj "/C=CN/ST=Chengdu/L=Chengdu/O=linux/OU=os/CN=koji/emailAddress=yifengyou666@gmail.com"

tree
ls -alh private/${caname}_ca_cert.key
ls -alh koji_ca_cert.crt

echo "All done!"
