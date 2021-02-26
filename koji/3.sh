#!/bin/bash

export caname=koji
for user in kojiadmin kojiuser ;
do
    echo "Common Name file with: ${user}"
    openssl genrsa -out certs/${user}.key 2048
    openssl req -config ssl.cnf -new -nodes -out certs/${user}.csr -key certs/${user}.key
    openssl ca -config ssl.cnf -keyfile private/${caname}_ca_cert.key -cert ${caname}_ca_cert.crt -out certs/${user}.crt -outdir certs -infiles certs/${user}.csr
    cat certs/${user}.crt certs/${user}.key > ${user}.pem
    openssl pkcs12 -export -inkey certs/${user}.key -in certs/${user}.crt -CAfile ${caname}_ca_cert.crt -out certs/${user}_browser_cert.p12
done
