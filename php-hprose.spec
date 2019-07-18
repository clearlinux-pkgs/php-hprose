#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-hprose
Version  : 1.6.8
Release  : 1
URL      : https://pecl.php.net//get/hprose-1.6.8.tgz
Source0  : https://pecl.php.net//get/hprose-1.6.8.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: php-hprose-lib = %{version}-%{release}
BuildRequires : buildreq-php

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

%description lib
lib components for the php-hprose package.


%prep
%setup -q -n hprose-1.6.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20180731/hprose.so
