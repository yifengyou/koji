#!/bin/bash

set -ex

cd /etc/pki/koji/


export caname=koji

for user in kojira kojiweb kojihub kojibuilder{1..5}; do
	set +x
	echo ""
	echo ""
	echo "Common Name fill with: ${user}"
	echo "Common Name fill with: ${user}"
	echo ""
	echo ""
	set -x
	openssl genrsa -out certs/${user}.key 2048
	openssl req -config ssl.cnf -new -nodes -out certs/${user}.csr -key certs/${user}.key
	openssl ca -config ssl.cnf -keyfile private/${caname}_ca_cert.key -cert ${caname}_ca_cert.crt 	-out certs/${user}.crt -outdir certs -infiles certs/${user}.csr
	cat certs/${user}.crt certs/${user}.key > ${user}.pem
done

echo "All done!"
