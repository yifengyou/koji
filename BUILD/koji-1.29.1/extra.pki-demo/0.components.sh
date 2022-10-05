#!/bin/bash

caname=koji
for user in kojira kojiweb kojihub kojibuilder1 kojibuilder2 kojibuilder3 ;
do
    openssl genrsa -out certs/${user}.key 2048
    openssl req -config ssl.cnf -new -nodes -out certs/${user}.csr -key certs/${user}.key
    openssl ca -config ssl.cnf -keyfile private/${caname}_ca_cert.key -cert ${caname}_ca_cert.crt -out certs/${user}.crt -outdir certs -infiles certs/${user}.csr
    cat certs/${user}.crt certs/${user}.key > ${user}.pem
done
echo "All done!"
