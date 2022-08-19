#!/bin/bash

set -xe

WORKDIR=`pwd`

cd /etc/pki/koji/

export CANAME=koji

for USER in kojira kojiweb kojihub kojibuilder{1..5}; do
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
		-subj "/C=CN/ST=Chengdu/L=Chengdu/O=linux/OU=os/CN=${USER}/emailAddress=yifengyou666@gmail.com"


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

echo "All done!"
