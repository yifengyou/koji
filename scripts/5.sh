#!/bin/bash

set -e

useradd kojiadmin || true

su - kojiadmin -c 'mkdir ~/.koji || true'
su - kojiadmin -c 'ls -alh ~/.koji'
su - kojiadmin -c 'cp -pv /etc/pki/koji/kojiadmin.pem ~/.koji/client.crt'
su - kojiadmin -c 'cp -pv /etc/pki/koji/koji_ca_cert.crt ~/.koji/clientca.crt'
su - kojiadmin -c 'cp -pv /etc/pki/koji/koji_ca_cert.crt ~/.koji/serverca.crt'
su - kojiadmin -c 'ls -alh ~/.koji'


cat > /etc/koji.conf << EOF
[koji]
server = http://192.168.66.130/kojihub
weburl = http://192.168.66.130/koji
topurl = http://192.168.66.130/kojifiles/
topdir = /mnt/koji
cert = ~/.koji/client.crt
ca = ~/.koji/clientca.crt
serverca = ~/.koji/serverca.crt
EOF

ls -alh /etc/koji.conf
cat /etc/koji.conf


useradd postgres || true
if [ -e /var/lib/pgsql/data ];then
	mv /var/lib/pgsql/data /tmp/data-${RANDOM}
fi
service postgresql initdb
service postgresql start
systemctl status postgresql --no-pager


echo "Add user koji"
useradd koji || true
passwd -d koji

echo "Create db koji"
su - postgres -c 'createuser koji || true'
su - postgres -c 'createdb -O koji koji || true'


echo "Import sql"
su - koji -c 'ls -alh /usr/share/doc/koji/docs/schema.sql'
su - koji -c 'psql koji koji < /usr/share/doc/koji/docs/schema.sql || true'


cat > /var/lib/pgsql/data/pg_hba.conf << EOF
host    koji            koji                                    trust
local   all             all                                     trust
host    all             all             127.0.0.1/32            trust
host    all             all             ::1/128                 trust
local   replication     all                                     peer
host    replication     all             127.0.0.1/32            ident
host    replication     all             ::1/128                 ident
EOF
ls -alh /var/lib/pgsql/data/pg_hba.conf 
cat /var/lib/pgsql/data/pg_hba.conf 

echo "Reload"
su - postgres -c 'pg_ctl reload -D /var/lib/pgsql/data'



echo "All done!"
