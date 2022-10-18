FROM rockylinux:8.6
LABEL maintainers="yifengyou <nicyou@tencent.com>"

RUN dnf install -y epel-release && cat /etc/yum.repos.d/*.repo && dnf makecache && \
    dnf -y --enablerepo powertools install systemd findutils gcc git \
                   which passwd openssh-server \
                   && \
    dnf install -y \
    nginx \
    sqlite vim && \
    dnf clean all
