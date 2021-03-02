#!/bin/bash

set -e

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


[ -e /etc/pki/koji ] && mv /etc/pki/koji /tmp/koji-${RANDOM}
mkdir -p /etc/pki/koji && cd /etc/pki/koji/ 

cat > /etc/pki/koji/ssl.cnf << EOF
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
default_bits            = 1024
default_keyfile         = privkey.pem
distinguished_name      = req_distinguished_name
attributes              = req_attributes
x509_extensions         = v3_ca # The extentions to add to the self signed cert
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
0.organizationName              = Organization Name (eg, company)
0.organizationName_default      = Linux
organizationalUnitName          = Organizational Unit Name (eg, section)
commonName                      = Common Name (eg, your name or your server\'s hostname)
commonName_max                  = 64
emailAddress                    = Email Address
emailAddress_default            = koji@163.com
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
tree
ls -alh private/${caname}_ca_cert.key

