FROM rockylinux:8.6
LABEL maintainers="yifengyou <nicyou@tencent.com>"

RUN dnf install -y epel-release && cat /etc/yum.repos.d/*.repo && dnf makecache && \
    dnf -y install systemd findutils git \
                   which passwd openssh-server vim \
                   && \
    dnf install -y \
        python3-pyOpenSSL \
        python3-mod_wsgi \
        postgresql-plpython3 \
        python3-kerberos \
        python3-cheetah \
        python3-multilib \
        httpd \
        mod_ssl \
        postgresql-server \
        koji \
        koji-hub \
        koji-hub-plugins \
        koji-builder \
        koji-builder-plugins \
        koji-web \
        koji-utils \
        python3-koji-cli-plugins \
        python3-koji-hub-plugins \
        createrepo \
        python3-mod_wsgi \
        sqlite python3-librepo \
	net-tools && \
    dnf clean all && mkdir -p /etc/koji-pki
RUN useradd koji && passwd -d koji
COPY files/service.koji /etc/service.koji
COPY files/koji-* /usr/bin/
COPY files/koji.conf /etc/koji.conf
COPY files/kojihub.conf /etc/httpd/conf.d/kojihub.conf
COPY files/hub.conf /etc/koji-hub/hub.conf
COPY files/kojira.conf /etc/kojira/kojira.conf
COPY files/web.conf /etc/kojiweb/web.conf
COPY files/koji-pki/* /etc/koji-pki/
COPY files/kojid.conf /etc/kojid/
COPY files/pg_hba.conf /etc/kojiweb/
COPY files/postgresql.conf /etc/kojiweb/
COPY files/daemon.py /usr/lib/python3.6/site-packages/koji/daemon.py
COPY files/__init__.py /usr/lib/python3.6/site-packages/koji/__init__.py
COPY files/ext/* /ext/
