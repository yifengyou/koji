#!/bin/bash

set -e

if [ -d /etc/pki/koji ];then
	rm -rf /etc/pki/koji
fi

mkdir -p /etc/pki/koji && cd /etc/pki/koji

cat >  /etc/pki/koji/ssl.cnf << EOF
HOME                    = .
RANDFILE                = .rand

[ca]
default_ca              = ca_default

[ca_default]
dir                     = .
certs                   = \$dir/certs
crl_dir                 = \$dir/crl
database                = \$dir/index.txt
new_certs_dir           = \$dir/newcerts
certificate             = \$dir/%s_ca_cert.pem
private_key             = \$dir/private/%s_ca_key.pem
serial                  = \$dir/serial
crl                     = \$dir/crl.pem
x509_extensions         = usr_cert
name_opt                = ca_default
cert_opt                = ca_default
default_days            = 3650
default_crl_days        = 30
default_md              = sha256
preserve                = no
policy                  = policy_match

[policy_match]
countryName             = match
stateOrProvinceName     = match
organizationName        = match
organizationalUnitName  = optional
commonName              = supplied
emailAddress            = optional

[req]
default_bits            = 2048
default_keyfile         = privkey.pem
default_md              = sha256
distinguished_name      = req_distinguished_name
attributes              = req_attributes
x509_extensions         = v3_ca # The extensions to add to the self signed cert
string_mask             = MASK:0x2002

[req_distinguished_name]
countryName                     = Country Name (2 letter code)
countryName_default             = CN
countryName_min                 = 2
countryName_max                 = 2
stateOrProvinceName             = State or Province Name (full name)
stateOrProvinceName_default     = Beijing
localityName                    = Locality Name (eg, city)
localityName_default            = Beijing
organizationName              = Organization Name (eg, company)
organizationName_default      = Linux
organizationalUnitName          = Organizational Unit Name (eg, section)
commonName                      = Common Name (eg, your name or your server\'s hostname)
commonName_max                  = 64
emailAddress                    = Email Address
emailAddress_default            = yifengyou666@gmail.com
emailAddress_max                = 64

[req_attributes]
challengePassword               = A challenge password
challengePassword_min           = 4
challengePassword_max           = 20
unstructuredName                = An optional company name

[usr_cert]
basicConstraints                = CA:FALSE
nsComment                       = "OpenSSL Generated Certificate"
subjectKeyIdentifier            = hash
authorityKeyIdentifier          = keyid,issuer:always

[v3_ca]
subjectKeyIdentifier            = hash
authorityKeyIdentifier          = keyid:always,issuer:always
basicConstraints                = CA:true
EOF

cat /etc/pki/koji/ssl.cnf


cd /etc/pki/koji/
mkdir {certs,private,confs}
touch index.txt
echo 01 > serial
openssl genrsa -out private/koji_ca_cert.key 2048
openssl rand -writerand .rand
openssl req -config ssl.cnf -new -x509 -days 3650 -key private/koji_ca_cert.key \
	-subj "/C=CN/ST=Beijing/L=Beijing/O=koji/CN=koji.com" \
	-out koji_ca_cert.crt -extensions v3_ca

export caname=koji
cat > /etc/pki/koji/confs/template << EOF
HOME                    = .
RANDFILE                = .rand

[ca]
default_ca              = ca_default

[ca_default]
dir                     = .
certs                   = \$dir/certs
crl_dir                 = \$dir/crl
database                = \$dir/index.txt
new_certs_dir           = \$dir/newcerts
certificate             = \$dir/%s_ca_cert.pem
private_key             = \$dir/private/%s_ca_key.pem
serial                  = \$dir/serial
crl                     = \$dir/crl.pem
x509_extensions         = usr_cert
name_opt                = ca_default
cert_opt                = ca_default
default_days            = 3650
default_crl_days        = 30
default_md              = sha256
preserve                = no
policy                  = policy_match

[policy_match]
countryName             = match
stateOrProvinceName     = match
organizationName        = match
organizationalUnitName  = optional
commonName              = supplied
emailAddress            = optional

[req]
default_bits            = 2048
default_keyfile         = privkey.pem
default_md              = sha256
distinguished_name      = req_distinguished_name
attributes              = req_attributes
x509_extensions         = v3_ca # The extensions to add to the self signed cert
string_mask             = MASK:0x2002

[req_distinguished_name]
countryName                     = Country Name (2 letter code)
countryName_default             = CN
countryName_min                 = 2
countryName_max                 = 2
stateOrProvinceName             = State or Province Name (full name)
stateOrProvinceName_default     = Beijing
localityName                    = Locality Name (eg, city)
localityName_default            = Beijing
organizationName                = Organization Name (eg, company)
organizationName_default        = Linux
organizationalUnitName          = Organizational Unit Name (eg, section)
organizationalUnitName_default  = insert_hostname
commonName                      = Common Name (eg, your name or your server\'s hostname)
commonName_max                  = 64
commonName_default              = insert_hostname
emailAddress                    = Email Address
emailAddress_default            = yifengyou666@gmail.com
emailAddress_max                = 64

[req_attributes]
challengePassword               = A challenge password
challengePassword_min           = 4
challengePassword_max           = 20
unstructuredName                = An optional company name

[usr_cert]
basicConstraints                = CA:FALSE
nsComment                       = "OpenSSL Generated Certificate"
subjectKeyIdentifier            = hash
authorityKeyIdentifier          = keyid,issuer:always

[v3_ca]
subjectKeyIdentifier            = hash
authorityKeyIdentifier          = keyid:always,issuer:always
basicConstraints                = CA:true
EOF

for user in kojira kojiweb kojihub kojibuilder{1..5};
do
    cat /etc/pki/koji/confs/template | sed 's/insert_hostname/'${user}'/'> ssl-${user}.cnf
    openssl genrsa -out certs/${user}.key 2048
    openssl req -config ssl-${user}.cnf -new -nodes \
	-subj "/C=CN/ST=Beijing/L=Beijing/O=koji/CN=${user}" \
	-out certs/${user}.csr \
	-key certs/${user}.key

    openssl ca -config ssl-${user}.cnf \
	-keyfile private/${caname}_ca_cert.key \
	-cert ${caname}_ca_cert.crt \
	-out certs/${user}.crt \
	-batch \
	-outdir certs -infiles certs/${user}.csr

    cat certs/${user}.crt certs/${user}.key > ${user}.pem
    mv ssl-${user}.cnf confs/
    echo "${user} certificate done!"
done

set -x
for user in kojiadmin kojiuser ;do
    cat /etc/pki/koji/confs/template | sed 's/insert_hostname/'${user}'/'> ssl-${user}.cnf
    openssl genrsa -out certs/${user}.key 2048
    openssl req -config ssl-${user}.cnf -new -nodes \
	-subj "/C=CN/ST=Beijing/L=Beijing/O=koji/CN=${user}" \
	-out certs/${user}.csr \
	-key certs/${user}.key

    openssl ca -config ssl-${user}.cnf \
	-keyfile private/${caname}_ca_cert.key \
	-cert ${caname}_ca_cert.crt \
	-out certs/${user}.crt \
	-batch \
	-outdir certs -infiles certs/${user}.csr
    cat certs/${user}.crt certs/${user}.key > ${user}.pem

    openssl pkcs12 -export \
	-inkey certs/${user}.key \
	-in certs/${user}.crt \
        -CAfile ${caname}_ca_cert.crt \
	-passout pass: \
	-out certs/${user}_browser_cert.p12

    mv ssl-${user}.cnf confs/
    echo "${user} certificate done!"
done

tree /etc/pki/koji

useradd kojiadmin || true
su - kojiadmin -c 'mkdir ~/.koji || true'
su - kojiadmin -c 'ls -alh ~/.koji'
su - kojiadmin -c 'cp -pv /etc/pki/koji/kojiadmin.pem ~/.koji/client.crt'
su - kojiadmin -c 'chown kojiadmin:kojiadmin ~/.koji/client.crt'
su - kojiadmin -c 'cp -pv /etc/pki/koji/koji_ca_cert.crt ~/.koji/clientca.crt'
su - kojiadmin -c 'chown kojiadmin:kojiadmin ~/.koji/clientca.crt'
su - kojiadmin -c 'cp -pv /etc/pki/koji/koji_ca_cert.crt ~/.koji/serverca.crt'
su - kojiadmin -c 'chown kojiadmin:kojiadmin ~/.koji/serverca.crt'
su - kojiadmin -c 'ls -alh ~/.koji'

echo "All done!no error!"

