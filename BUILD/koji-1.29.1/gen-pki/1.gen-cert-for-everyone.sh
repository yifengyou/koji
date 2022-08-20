#!/bin/bash

set -xe

WORKDIR=`pwd`
cd /etc/pki/koji/
export CANAME=koji

for USER in kojiadmin kojira kojiweb kojihub kojibuilder{1..5}; do
	if [ -f certs/${USER}/${USER}.pem ]
	then
		echo "already exists /etc/pki/koji/${USER}/${USER}.pem, skip"
		continue
	fi
	mkdir certs/${USER}
	openssl genrsa -out certs/${USER}/${USER}.key 2048

	openssl req \
		-config ssl.cnf \
		-new -nodes \
		-out certs/${USER}/${USER}.csr \
		-key certs/${USER}/${USER}.key \
		-subj "/C=CN/ST=Chengdu/L=Chengdu/O=Linux/OU=OS/CN=${USER}/emailAddress=yifengyou666@gmail.com"

	openssl ca -batch \
		-config ssl.cnf \
		-keyfile private/${CANAME}_ca_cert.key \
		-cert ${CANAME}_ca_cert.crt \
		-out certs/${USER}/${USER}.crt \
		-outdir certs/${USER} \
		-infiles certs/${USER}/${USER}.csr

	cat certs/${USER}/${USER}.crt certs/${USER}/${USER}.key > certs/${USER}/${USER}.pem
done

tree /etc/pki/koji/

# 当前用户作为koji超级管理员
[ -d ~/.koji ] || mkdir ~/.koji
/usr/bin/cp -a /etc/pki/koji/certs/kojiadmin/kojiadmin.pem ~/.koji/client.crt
/usr/bin/cp /etc/pki/koji/koji_ca_cert.crt ~/.koji/clientca.crt
/usr/bin/cp /etc/pki/koji/koji_ca_cert.crt ~/.koji/serverca.crt

echo "All done!"
