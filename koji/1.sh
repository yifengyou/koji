#!/bin/bash

set -ex
mkdir -p /etc/pki/koji || true
cd /etc/pki/koji/ 

if [ -e certs ];then
	echo "Already have certs"
	exit 1
fi

mkdir {certs,private} 

touch index.txt 
echo 01 > serial 
export caname=koji 

openssl genrsa -out private/${caname}_ca_cert.key 2048 

echo "Common Name fill with koji"
echo "Common Name fill with koji"
echo "Common Name fill with koji"
echo "Common Name fill with koji"

openssl req -config ssl.cnf -new -x509 -days 3650 -key private/${caname}_ca_cert.key -out ${caname}_ca_cert.crt -extensions v3_ca

echo "All done!"
