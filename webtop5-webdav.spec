Summary: WebTop WebDAV integration
Name: webtop5-webdav
Version: 0.0.1
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name}
Source0: https://github.com/sonicle-webtop/webtop-dav-server/archive/master.tar.gz
Source1: webtop5-webdav.conf
Source1: config.json
BuildArch: noarch

Requires: webtop5
Requires: php-common

BuildRequires: php-cli

%description
NethServer DAV implementation for WebTop 5

%prep
%setup -n webdav

%build
mkdir -p root/usr/share/webtop/webdav/
mkdir -p root/etc/httpd/conf.d/
tar xvzf %{SOURCE0} --exclude='.gitignore' -C root/usr/share/webtop/webdav
cp %{SOURCE1} root/etc/httpd/conf.d/

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})


%files
%defattr(-,root,root)
%config /etc/httpd/conf.d/webtop5-webdav.conf
%config /usr/share/webtop/webdav/config.json
/usr/share/webtop/webdav/.htaccess
/usr/share/webtop/webdav/*

%changelog
