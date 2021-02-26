#!/bin/bash

#yum install pyOpenSSL python-krbV mod_wsgi postgresql-python mod_auth_kerb python-cheetah httpd mod_ssl postgresql-server koji koji-hub koji-web

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
	postgresql-server \
	python3-mod_wsgi

