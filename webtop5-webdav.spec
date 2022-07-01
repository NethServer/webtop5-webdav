%define wtrelease 5.17.1

Summary: WebTop WebDAV integration
Name: webtop5-webdav
Version: 1.0.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name}
Source0: https://github.com/sonicle-webtop/webtop-dav-server/archive/wt-%{wtrelease}.tar.gz
Source1: webtop5-webdav.conf
Source2: config.json
Source3: webtop-dav
BuildArch: noarch

Requires: webtop5
Requires: rh-php73-php-fpm, rh-php73-php-mbstring

%description
NethServer DAV implementation for WebTop 5


%build
mkdir -p root/usr/share/webtop/
mkdir -p root/etc/httpd/conf.d/
mkdir -p root/var/log/webtop-dav/
mkdir -p root/etc/logrotate.d/
tar xvzf %{SOURCE0} --exclude='.gitignore'
mv webtop-dav-server-wt-%{wtrelease}/src root/usr/share/webtop/webdav
cp %{SOURCE1} root/etc/httpd/conf.d/
cp %{SOURCE2} root/usr/share/webtop/webdav/
cp %{SOURCE3} root/etc/logrotate.d/

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})


%files
%defattr(-,root,root)
%config /etc/httpd/conf.d/webtop5-webdav.conf
%config /usr/share/webtop/webdav/config.json
%dir %attr(-,apache,apache) /var/log/webtop-dav
/etc/logrotate.d/webtop-dav
/usr/share/webtop/webdav/.htaccess
/usr/share/webtop/webdav/.user.ini
/usr/share/webtop/webdav/*

%changelog
* Fri Jul 01 2022 Matteo Valentini <matteo.valentini@nethesis.it> - 1.0.1-1
- WebTop 5.17.3 - NethServer/dev#6674

* Thu Feb 03 2022 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- WebTop: use PHP 7.3 for sabredav and z-push - NethServer/dev#6632

* Thu Oct 10 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.3.0-1
- Webtop: broken webdav syncronization  - Bug NethServer/dev#5862

* Tue Oct 01 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 0.2.0-1
- WebTop 5.7.3 - NethServer/dev#5770

* Tue Mar 26 2019 Matteo Valentini <matteo.valentini@nethesis.it> - 0.1.2-1
- WebTop 5.6.3 - NethServer/dev#5729

* Tue Feb 12 2019 Matteo Valentini <matteo.valentini@nethesis.it> - 0.1.1-1
- WebTop 5.5.2 - NethServer/dev#5706
  - Update to upstream release 5.5.1

* Thu Dec 13 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 0.1.0-1
-  WebTop 5.5.0 - NethServer/dev#5666
  - httpd conf: change php fcgi listen port (php 7.1)
  - rpm spec: switch from php 5.6 to php 7.1

* Tue Jul 17 2018 Matteo Valentini <matteo.valentini@nethesis.it> - 0.0.2-1
- WebTop 5.2.3 - NethServer/dev#5516

