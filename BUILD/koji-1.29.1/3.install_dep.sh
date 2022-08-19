#!/bin/bash

set -x

yum install -y python3-librepo
pip3 install -r requirements.txt


echo "All done!"

exit 0


yum install -y python3-pyOpenSSL \
	python3-mod_wsgi \
	postgresql-plpython3 \
	python3-kerberos \
	python3-cheetah \
	httpd \
	mod_ssl \
	postgresql-server \
	koji \
	koji-hub \
	koji-web \
	koji-utils \
	createrepo \
	postgresql-server \
	python3-mod_wsgi
