#!/bin/bash

set -e


yum install postgresql-server -y

postgresql-setup --initdb --unit postgresql || true

systemctl enable postgresql --now

useradd koji || true
echo 'koji:kojipasswd' | chpasswd

su - postgres -c 'createuser --no-superuser --no-createrole --no-createdb koji'
su - postgres -c 'createdb -O koji koji'
su - postgres -c "psql -c \"alter user koji with encrypted password 'mypassword';\""

yum install -y koji
su - koji -c 'psql koji koji < /usr/share/doc/koji*/docs/schema.sql'

echo "All done!no error!"
