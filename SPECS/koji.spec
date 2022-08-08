# This package depends on selective manual byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 0

%define __python %{__python3}

# If the definition isn't available for python3_pkgversion, define it
%{?!python3_pkgversion:%global python3_pkgversion 3}

Name: koji
Version: 1.29.1
Release: 1%{?dist}
# the included arch lib from yum's rpmUtils is GPLv2+
License: LGPLv2 and GPLv2+
Summary: Build system tools
URL: https://pagure.io/koji/
Source0: https://releases.pagure.org/koji/koji-%{version}.tar.bz2

# Not upstreamable
Patch100: fedora-config.patch

BuildArch: noarch
Requires: python%{python3_pkgversion}-%{name} = %{version}-%{release}
Requires: python%{python3_pkgversion}-libcomps
Requires: python3-libcomps
BuildRequires: systemd
BuildRequires: pkgconfig
BuildRequires: sed

%description
Koji is a system for building and tracking RPMS.  The base package
contains shared libraries and the command-line interface.

%package -n python%{python3_pkgversion}-%{name}
Summary: Build system tools python library
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: make
BuildRequires: python3-pip
BuildRequires: python3-wheel
Requires: python%{python3_pkgversion}-rpm
Requires: python%{python3_pkgversion}-requests
Requires: python%{python3_pkgversion}-requests-gssapi
Requires: python%{python3_pkgversion}-dateutil
Requires: python%{python3_pkgversion}-six

%description -n python%{python3_pkgversion}-%{name}
Koji is a system for building and tracking RPMS.
This subpackage provides python functions and libraries.

%package -n python%{python3_pkgversion}-%{name}-cli-plugins
Summary: Koji client plugins
License: LGPLv2
Requires: python%{python3_pkgversion}-%{name} = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}-cli-plugins
Plugins to the koji command-line interface

%package hub
Summary: Koji XMLRPC interface
License: LGPLv2
Requires: %{name} = %{version}-%{release}
Requires: %{name}-hub-code
%if 0%{?fedora} || 0%{?rhel} > 7
Suggests: python%{python3_pkgversion}-%{name}-hub
Suggests: python%{python3_pkgversion}-%{name}-hub-plugins
%endif

%description hub
koji-hub is the XMLRPC interface to the koji database

%package -n python%{python3_pkgversion}-%{name}-hub
Summary: Koji XMLRPC interface
License: LGPLv2 and GPLv2
# rpmdiff lib (from rpmlint) is GPLv2 (only)
Requires: httpd
Requires: python%{python3_pkgversion}-mod_wsgi
Requires: mod_auth_gssapi
Requires: python%{python3_pkgversion}-psycopg2
Requires: python%{python3_pkgversion}-%{name} = %{version}-%{release}
Provides: %{name}-hub-code = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}-hub
koji-hub is the XMLRPC interface to the koji database

%package hub-plugins
Summary: Koji hub plugins
License: LGPLv2
Requires: %{name}-hub-plugins-code = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} > 7
Suggests: python%{python3_pkgversion}-%{name}-hub-plugins
%endif

%description hub-plugins
Plugins to the koji XMLRPC interface

%package -n python%{python3_pkgversion}-%{name}-hub-plugins
Summary: Koji hub plugins
License: LGPLv2
Requires: python%{python3_pkgversion}-%{name}-hub = %{version}-%{release}
Requires: python%{python3_pkgversion}-qpid-proton
Requires: cpio
Provides: %{name}-hub-plugins-code = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}-hub-plugins
Plugins to the koji XMLRPC interface

%package builder-plugins
Summary: Koji builder plugins
License: LGPLv2
Requires: %{name} = %{version}-%{release}
Requires: %{name}-builder = %{version}-%{release}

%description builder-plugins
Plugins for the koji build daemon

%package builder
Summary: Koji RPM builder daemon
License: LGPLv2
Requires: mock >= 0.9.14
Requires(pre): /usr/sbin/useradd
Requires: squashfs-tools
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: /usr/bin/cvs
Requires: /usr/bin/svn
Requires: /usr/bin/git
Requires: createrepo_c >= 0.10.0
Requires: python%{python3_pkgversion}-%{name} = %{version}-%{release}
Requires: python%{python3_pkgversion}-librepo
Requires: python%{python3_pkgversion}-multilib
Requires: python%{python3_pkgversion}-cheetah
Requires: python%{python3_pkgversion}-pycdio

%description builder
koji-builder is the daemon that runs on build machines and executes
tasks that come through the Koji system.

%package vm
Summary: Koji virtual machine management daemon
License: LGPLv2
Requires: %{name} = %{version}-%{release}
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: python%{python3_pkgversion}-libvirt
Requires: python%{python3_pkgversion}-libxml2
Requires: /usr/bin/virt-clone
Requires: qemu-img

%description vm
koji-vm contains a supplemental build daemon that executes certain tasks in a
virtual machine. This package is not required for most installations.

%package utils
Summary: Koji Utilities
License: LGPLv2
Requires: %{name} = %{version}-%{release}
Requires: python%{python3_pkgversion}-psycopg2
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description utils
Utilities for the Koji system

%package web
Summary: Koji Web UI
License: LGPLv2
Requires: %{name} = %{version}-%{release}
Requires: %{name}-web-code = %{version}-%{release}
%if 0%{?fedora} || 0%{?rhel} > 7
Suggests: python%{python3_pkgversion}-%{name}-web
%endif

%description web
koji-web is a web UI to the Koji system.

%package -n python%{python3_pkgversion}-%{name}-web
Summary: Koji Web UI
License: LGPLv2
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}-web}
Requires: httpd
Requires: python%{python3_pkgversion}-mod_wsgi
Requires: mod_auth_gssapi
Requires: python%{python3_pkgversion}-psycopg2
Requires: python%{python3_pkgversion}-cheetah
Requires: python%{python3_pkgversion}-%{name} = %{version}-%{release}
Provides: %{name}-web-code = %{version}-%{release}

%description -n python%{python3_pkgversion}-%{name}-web
koji-web is a web UI to the Koji system.

%prep
%autosetup -p1
# we'll be packaging these separately and don't want them registered
# to the wheel we will produce.
sed -e '/util\/koji/g' -e '/koji_cli_plugins/g' -i setup.py

%build
# 宏展开
# %%py3_build_wheel() %%{expand:\\\
#   CFLAGS="${CFLAGS:-${RPM_OPT_FLAGS}}" LDFLAGS="${LDFLAGS:-${RPM_LD_FLAGS}}"\\\
#   %%{__python3} %%{py_setup} %%{?py_setup_args} bdist_wheel %%{?*}
#   sleep 1
# }
# bdist             create a built (binary) distribution
# python3 setup.py bdist
%py3_build_wheel

%install
%py3_install_wheel %{name}-%{version}-py3-none-any.whl
mkdir -p %{buildroot}/etc/koji.conf.d
cp cli/koji.conf %{buildroot}/etc/koji.conf
for D in hub builder plugins util www vm ; do
    pushd $D
    make DESTDIR=$RPM_BUILD_ROOT PYTHON=%{__python3} %{?install_opt} install
    popd
done

# alter python interpreter in koji CLI
scripts='%{_bindir}/koji %{_sbindir}/kojid %{_sbindir}/kojira %{_sbindir}/koji-shadow
         %{_sbindir}/koji-gc %{_sbindir}/kojivmd %{_sbindir}/koji-sweep-db
         %{_sbindir}/koji-sidetag-cleanup'
for fn in $scripts ; do
    sed -i 's|#!/usr/bin/python2|#!/usr/bin/python3|' $RPM_BUILD_ROOT$fn
done

# handle extra byte compilation
extra_dirs='
    %{_prefix}/lib/koji-builder-plugins
    %{_prefix}/koji-hub-plugins
    %{_datadir}/koji-hub
    %{_datadir}/koji-web/lib/kojiweb
    %{_datadir}/koji-web/scripts'
for fn in $extra_dirs ; do
    %py_byte_compile %{__python3} %{buildroot}$fn
done

%files
%{_bindir}/*
%config(noreplace) /etc/koji.conf
%dir /etc/koji.conf.d
%doc docs Authors COPYING LGPL

%files -n python%{python3_pkgversion}-koji
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}.*-info
%{python3_sitelib}/koji_cli

%files -n python%{python3_pkgversion}-%{name}-cli-plugins
%{python3_sitelib}/koji_cli_plugins
# we don't have config files for default plugins yet
#%%dir %%{_sysconfdir}/koji/plugins
#%%config(noreplace) %%{_sysconfdir}/koji/plugins/*.conf

%files hub
%config(noreplace) /etc/httpd/conf.d/kojihub.conf
%dir /etc/koji-hub
%config(noreplace) /etc/koji-hub/hub.conf
%dir /etc/koji-hub/hub.conf.d
%{_sbindir}/koji-sweep-db
%{_unitdir}/koji-sweep-db.service
%{_unitdir}/koji-sweep-db.timer

%files -n python%{python3_pkgversion}-%{name}-hub
%{_datadir}/koji-hub/*.py
%{_datadir}/koji-hub/__pycache__

%files hub-plugins
%dir /etc/koji-hub/plugins
%config(noreplace) /etc/koji-hub/plugins/*.conf

%files -n python%{python3_pkgversion}-%{name}-hub-plugins
%{_prefix}/lib/koji-hub-plugins/*.py
%{_prefix}/lib/koji-hub-plugins/__pycache__

%files builder-plugins
%dir /etc/kojid/plugins
%config(noreplace) /etc/kojid/plugins/*.conf
%dir %{_prefix}/lib/koji-builder-plugins
%{_prefix}/lib/koji-builder-plugins/*.py*
%{_prefix}/lib/koji-builder-plugins/__pycache__

%files utils
%{_sbindir}/kojira
%{_unitdir}/koji-gc.service
%{_unitdir}/koji-gc.timer
%{_unitdir}/kojira.service
%dir /etc/kojira
%config(noreplace) /etc/kojira/kojira.conf
%{_sbindir}/koji-gc
%dir /etc/koji-gc
%config(noreplace) /etc/koji-gc/koji-gc.conf
%config(noreplace) /etc/koji-gc/email.tpl
%{_sbindir}/koji-shadow
%dir /etc/koji-shadow
%{_sbindir}/koji-sidetag-cleanup
%config(noreplace) /etc/koji-shadow/koji-shadow.conf

%files web
%dir /etc/kojiweb
%config(noreplace) /etc/kojiweb/web.conf
%config(noreplace) /etc/httpd/conf.d/kojiweb.conf
%dir /etc/kojiweb/web.conf.d

%files -n python%{python3_pkgversion}-%{name}-web
%{_datadir}/koji-web

%files builder
%{_sbindir}/kojid
%{_unitdir}/kojid.service
%dir /etc/kojid
%config(noreplace) /etc/kojid/kojid.conf
%attr(-,kojibuilder,kojibuilder) /etc/mock/koji

%pre builder
/usr/sbin/useradd -r -s /bin/bash -G mock -d /builddir -M kojibuilder 2>/dev/null ||:

%post builder
%systemd_post kojid.service

%preun builder
%systemd_preun kojid.service

%postun builder
%systemd_postun kojid.service

%files vm
%{_sbindir}/kojivmd
#dir %%{_datadir}/kojivmd
%{_datadir}/kojivmd/kojikamid
%{_unitdir}/kojivmd.service
%dir /etc/kojivmd
%config(noreplace) /etc/kojivmd/kojivmd.conf

%post vm
%systemd_post kojivmd.service

%preun vm
%systemd_preun kojivmd.service

%postun vm
%systemd_postun kojivmd.service

%post utils
%systemd_post kojira.service

%preun utils
%systemd_preun kojira.service

%postun utils
%systemd_postun kojira.service

%changelog
* Tue Jul 12 2022 Kevin Fenzi <kevin@scrye.com> - 1.29.1-1
- Update to 1.29.1. Fiex rhbz#2106294

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.29.0-2
- Rebuilt for Python 3.11

* Fri May 27 2022 Kevin Fenzi <kevin@scrye.com> - 1.29.0-1
- Update to 1.29.0. Fixes rhbz#2090641

* Thu Apr 07 2022 Kevin Fenzi <kevin@scrye.com> - 1.28.1-1
- Update to 1.28.1. Fixes rhbz#2072899

* Mon Feb 21 2022 Kevin Fenzi <kevin@scrye.com> - 1.28.0-1
- Update to 1.28.0. Fixes rhbz#2056503

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Kevin Fenzi <kevin@scrye.com> - 1.27.1-1
- Update to 1.27.1. Fixes rhbz#2040251

* Tue Nov 23 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.27.0-3
- Correct topurl in fedora-config.patch. Fixes rhbz#2025562

* Thu Nov 18 2021 Kevin Fenzi <kevin@scrye.com> - 1.27.0-2
- Fix rebasing issue in koji.conf

* Thu Nov 18 2021 Kevin Fenzi <kevin@scrye.com> - 1.27.0-1
- Update to 1.27.0. Fixes rhbz#2024552

* Sun Oct 10 2021 Kevin Fenzi <kevin@scrye.com> - 1.26.1-1
- Update to 1.26.1. Fixes rhbz#2011804

* Fri Sep 10 2021 Carl George <carl@george.computer> - 1.26.0-2
- Remove duplicate dist provides that are now automatic

* Wed Aug 25 2021 Kevin Fenzi <kevin@scrye.com> - 1.26.0-1
- Update to 1.26.0. Fixes rhbz#1996614

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.25.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 01 2021 Kevin Fenzi <kevin@scrye.com> - 1.25.1-1
- Update to 1.25.1. Fixes rhbz#1978116

* Tue Jun 15 2021 Jiri Popelka <jpopelka@redhat.com> - 1.25.0-3
- Python egginfo. Fixes rhbz#1968618

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.25.0-2
- Rebuilt for Python 3.10

* Thu May 20 2021 Kevin Fenzi <kevin@scrye.com> - 1.25.0-1
- Update to 1.25.0. Fixes rhbz#1962636

* Tue Apr 13 2021 Kevin Fenzi <kevin@scrye.com> - 1.24.1-1
- Update to 1.24.1. Fixes rhbz#1948545

* Thu Feb 18 2021 Kevin Fenzi <kevin@scrye.com> - 1.24.0-1
- Update to 1.24.0. Fixes rhbz#1930032

* Thu Jan 28 2021 Kevin Fenzi <kevin@scrye.com> - 1.23.1-1
- Update to 1.23.1. Fixes rhbz#1917340

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.23.0-3
- Fixup compatibility of kojid with koji-hub 1.21

* Mon Nov 30 2020 Kevin Fenzi <kevin@scrye.com> - 1.23.0-2
- Fix 32 bit arm install issue. Fixes bug #1894261

* Thu Oct 22 2020 Kevin Fenzi <kevin@scrye.com> - 1.23.0-1
- Update to 1.23.0. Fixes bug #1890435

* Mon Sep 07 2020 Kevin Fenzi <kevin@scrye.com> - 1.22.1-1
- Update to 1.22.1. Fixes 1876427

* Wed Aug 12 2020 Kevin Fenzi <kevin@scrye.com> - 1.22.0-2
- Change Requires to python3-libcomps, the epel8 one doesn't provide python-libcomps

* Sun Aug 02 2020 Kevin Fenzi <kevin@scrye.com> - 1.22.0-1
- Update to 1.22.0.
- Remove python2 suppport, move to python3 on everything except epel6/7

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 12 2020 Kevin Fenzi <kevin@scrye.com> - 1.21.1-1
- Update to 1.21.1. (really this time!)

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.21.0-3
- Rebuilt for Python 3.9

* Thu Apr 30 2020 Kevin Fenzi <kevin@scrye.com> - 1.21.0-2
- Add patch to fix issue with admins not being able to force tagging. 
- Fixes https://pagure.io/koji/issue/2202 upstream.

* Tue Apr 21 2020 Kevin Fenzi <kevin@scrye.com> - 1.21.0-1
- Update to 1.21.0. Fixes bug #1826406

* Fri Mar 06 2020 Kevin Fenzi <kevin@scrye.com> - 1.20.1-1
- Update to 1.20.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Kevin Fenzi <kevin@scrye.com> - 1.20.0-1
- Update to 1.20.0.

* Wed Nov 27 2019 Kevin Fenzi <kevin@scrye.com> - 1.19.1-2
- Add Requires to koji builder on python3-pycdio/pycdio. Fixes bug #1775536

* Fri Nov 08 2019 Kevin Fenzi <kevin@scrye.com> - 1.19.1-1
- Update to 1.19.1

* Fri Nov 01 2019 Mohan Boddu <mboddu@bhujji.com> - 1.19.0-1
- Rebase to 1.19.0
- Removing downstream patch 1613

* Wed Oct 09 2019 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.18.1-1
- Rebase to 1.18.1 for CVE-2019-17109

* Wed Sep 18 2019 Jiri Popelka <jpopelka@redhat.com> - 1.18.0-6
- Fix macro added in previous change.

* Tue Sep 17 2019 Kevin Fenzi <kevin@scrye.com> - 1.18.0-5
- Add provides for python3 subpackage. Fixes bug #1750391

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.18.0-4
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Kevin Fenzi <kevin@scrye.com> - 1.18.0-3
- Fix pkgsurl/topurl default mistake.

* Fri Aug 16 2019 Kevin Fenzi <kevin@scrye.com> - 1.18.0-2
- Fix mergerepos conditional for f30.

* Fri Aug 16 2019 Kevin Fenzi <kevin@scrye.com> - 1.18.0-1
- Update to 1.18.0.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Kevin Fenzi <kevin@scrye.com> - 1.17.0-7
- Add patch to fix koji kerberos auth with python3.
- Drop internal mergerepos so we can go all python3. Fixes bug #1715257

* Wed May 29 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.17.0-7
- Expose dynamic_buildrequires mock setting

* Tue May 28 2019 Kevin Fenzi <kevin@scrye.com> - 1.17.0-6
- Switch kojid back to python3 as imagefactory and oz have moved.
- Backport patch to download only repomd.xml instead of all repodata.
- Backport patch to allow 'bare' repo merging for modularity.
- Backport patch to allow for seperate srpm repos in buildroot repos.

* Mon Mar 11 2019 Neal Gompa <ngompa13@gmail.com> - 1.17.0-5
- Switch kojid back to Python 2 so that imgfac doesn't get disabled

* Sun Mar 10 2019 Neal Gompa <ngompa13@gmail.com> - 1.17.0-4
- Add patch proposed upstream to use createrepo_c by default to drop yum dependency

* Sun Mar 10 2019 Neal Gompa <ngompa13@gmail.com> - 1.17.0-3
- Remove remnants of unused /usr/libexec/koji-hub

* Thu Mar 07 2019 Neal Gompa <ngompa13@gmail.com> - 1.17.0-2
- Enable Python 3 for Fedora 30+ and EL8+
- Sync packaging changes from upstream

* Thu Mar 07 2019 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.17.0-1
- Rebase to 1.17.0

* Thu Feb 21 2019 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.16.2-1
- Rebase to 1.16.2 for CVE-2018-1002161

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Adam Williamson <awilliam@redhat.com> - 1.16.1-3
- Backport fix for Python 3 connection failure bug (#1192, PR #1203)

* Fri Sep 14 2018 Kevin Fenzi <kevin@scrye.com> - 1.16.1-2
- Fix bad sed that caused python32 dep.

* Thu Sep 13 2018 Kevin Fenzi <kevin@scrye.com> - 1.16.1-1
- Update to 1.16.1

* Tue Jul 31 2018 Kevin Fenzi <kevin@scrye.com> - 1.16.0-1
- Update to 1.16.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.15.1-2
- Rebuilt for Python 3.7

* Tue Apr 03 2018 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.15.1-1
- Rebase to 1.15.1
- Fixes CVE-2018-1002150

* Fri Mar 16 2018 Kevin Fenzi <kevin@scrye.com> - 1.15.0-7
- Backport PR #841 to allow configurable timeout for oz

* Tue Feb 20 2018 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.15.0-6
- Backport PR #796

* Sun Feb 18 2018 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.15.0-5
- Add  workaround patch for bug #808

* Fri Feb 16 2018 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.15.0-4
- Backport patch from PR#794
- Fix macro escaping in comments

* Mon Feb 12 2018 Owen Taylor <otaylor@redhat.com> - 1.15.0-3
- Make hub, builder, etc, require python2-koji not koji

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.15.0-1
- Rebase to koji 1.15.0

* Mon Jan 22 2018 Troy Dawson <tdawson@redhat.com> - 1.14.0-4
- Update conditional

* Thu Dec 07 2017 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.14.0-3
- Backport py3 runroot encoding patch (PR#735)

* Mon Dec 04 2017 Patrick Uiterwijk <patrick@puiterwijk.org> - 1.14.0-2
- Backport py3 keytab patch (PR#708)
- Backport patches for exit code (issue#696)

* Tue Sep 26 2017 Dennis Gilmore <dennis@ausil.us> - 1.14.0-1
- update to upstream 1.14.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 1.13.0-3
- Remove the 2 postfix for pycurl and libcomps on RHEL

* Tue Jul 11 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 1.13.0-2
- Require python2-koji on Fedora <= 26.

* Mon Jul 03 2017 Dennis Gilmore <dennis@ausil.us> - 1.13.0-1
- update to upstream 1.13.0
- remove old  changelog entries
