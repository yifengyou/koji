#!/bin/bash

set -x

koji build rockylinux9-addons --skip-tag  --nowait   'git+https://git.rockylinux.org/staging/src/rocky-release#origin/r9'

exit 0

koji build rockylinux9-addons --skip-tag  --nowait   'git+https://git.rockylinux.org/staging/rpms/pytest#origin/r9'

koji build rockylinux9-addons --skip-tag  --nowait   'git+https://git.rockylinux.org/staging/rpms/python-jinja2#origin/r9'

koji build rockylinux9-addons --skip-tag  --nowait   'git+https://git.rockylinux.org/staging/rpms/python-flask#origin/r9'











exit 0

koji build rockylinux9-addons --skip-tag  --nowait   'git+https://git.rockylinux.org/staging/rpms/cockpit#origin/r9'

koji build rockylinux9-addons --skip-tag  --nowait   'git+https://git.rockylinux.org/staging/src/rocky-release#a0178fce33dadc1170be3102d6cb84c6ac0d1729'

koji build rockylinux9-addons --skip-tag  --nowait   'git+https://git.rockylinux.org/staging/src/rocky-release?SPECS#a0178fce33dadc1170be3102d6cb84c6ac0d1729'

koji build rockylinux9-addons --skip-tag 'git+https://git.centos.org/rpms/centos-repos.git#b759b17557b9577e8ea156740af0249ab1a22d70'

koji build rockylinux9-addons --skip-tag 'git+https://git.rockylinux.org/staging/src/rocky-release#a0178fce33dadc1170be3102d6cb84c6ac0d1729'

koji build rockylinux9-addons --skip-tag 'git+https://git.rockylinux.org/staging/src/rocky-release?SPECS#a0178fce33dadc1170be3102d6cb84c6ac0d1729'

koji build rockylinux9-addons --skip-tag 'git+https://git.rockylinux.org/staging/src/rocky-release?SPECS#origin/r9'

koji build rockylinux9-addons --skip-tag 'git+https://git.rockylinux.org/staging/src/rocky-release?rocky-release#origin/r9'

koji build rockylinux9-addons --skip-tag 'git+https://git.rockylinux.org/staging/src/rocky-release?staging/src/rocky-release#r9'

koji build rockylinux9-addons --skip-tag 'git+https://git.rockylinux.org/staging/src/rocky-release'

koji build rockylinux9-addons curl-7.61.1-25.el8.src.rpm --skip-tag

koji build --scratch rawhide 'https://git.rockylinux.org/staging/src/rocky-release'

koji build dist-centos6 --scratch 'git+ssh://git@github.com/github-username/reponame.git?jetty/8.1.9/#HEAD

