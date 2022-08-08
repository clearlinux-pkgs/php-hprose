#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-hprose
Version  : 1.8.0
Release  : 16
URL      : https://pecl.php.net/get/hprose-1.8.0.tgz
Source0  : https://pecl.php.net/get/hprose-1.8.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: php-hprose-lib = %{version}-%{release}
Requires: php-hprose-license = %{version}-%{release}
BuildRequires : buildreq-php
Patch1: PHP-8.patch

%description
# Hprose extension for PHP
[![Join the chat at https://gitter.im/hprose/hprose-pecl](https://img.shields.io/badge/GITTER-join%20chat-green.svg)](https://gitter.im/hprose/hprose-pecl?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/hprose/hprose-pecl.svg)](https://travis-ci.org/hprose/hprose-pecl)
![Supported PHP versions: 5.2 .. 7.3](https://img.shields.io/badge/php-5.2~7.4-blue.svg)
[![GitHub release](https://img.shields.io/github/release/hprose/hprose-pecl.svg)](https://github.com/hprose/hprose-pecl/releases)
[![License](https://img.shields.io/github/license/hprose/hprose-pecl.svg)](http://opensource.org/licenses/MIT)

%package lib
Summary: lib components for the php-hprose package.
Group: Libraries
Requires: php-hprose-license = %{version}-%{release}

%description lib
lib components for the php-hprose package.


%package license
Summary: license components for the php-hprose package.
Group: Default

%description license
license components for the php-hprose package.


%prep
%setup -q -n hprose-1.8.0
cd %{_builddir}/hprose-1.8.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-hprose
cp %{_builddir}/hprose-1.8.0/LICENSE.md %{buildroot}/usr/share/package-licenses/php-hprose/22cb455f6bcf1953cc56ca486162963d8a497268
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/hprose.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-hprose/22cb455f6bcf1953cc56ca486162963d8a497268
