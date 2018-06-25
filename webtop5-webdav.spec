%define wtrelease 5.2.1

Summary: WebTop WebDAV integration
Name: webtop5-webdav
Version: 0.0.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name}
Source0: https://github.com/sonicle-webtop/webtop-dav-server/archive/wt-%{wtrelease}.tar.gz
Source1: webtop5-webdav.conf
Source3: webtop-dav
BuildArch: noarch

Requires: webtop5
Requires: rh-php56-php-fpm, rh-php56-php-mbstring

%description
NethServer DAV implementation for WebTop 5


%build
mkdir -p root/usr/share/webtop/
mkdir -p root/etc/httpd/conf.d/
mkdir -p root/var/log/webtop-dav/
mkdir -p root/etc/logrotate.d/
tar xvzf %{SOURCE0} --exclude='.gitignore'
#pushd webtop-dav-server-master
#chmod a+x ./bin/*
#./bin/make-dav-client.sh
#popd
mv webtop-dav-server-wt-%{wtrelease}/src root/usr/share/webtop/webdav
cp %{SOURCE1} root/etc/httpd/conf.d/
cp %{SOURCE3} root/etc/logrotate.d/

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})


%files
%defattr(-,root,root)
%config /etc/httpd/conf.d/webtop5-webdav.conf
%dir %attr(-,apache,apache) /var/log/webtop-dav
/etc/logrotate.d/webtop-dav
/usr/share/webtop/webdav/.htaccess
/usr/share/webtop/webdav/*

%changelog
