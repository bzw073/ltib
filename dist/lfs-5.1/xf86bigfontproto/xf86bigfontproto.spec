%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : XF86bigfont proto
Name            : xf86bigfontproto
Version         : 1.1.2
Release         : 1
License         : X11
Vendor          : X.Org Foundation
Packager        : ProFUSION embedded systems <contact@profusion.mobi>
Group           : System Environment/Libraries
URL             : http://www.x.org/
Source          : %{name}-%{version}.tar.bz2
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
XFree86 bigfont proto package.

%Prep
%setup

%Build
./configure --prefix=%{_prefix} --host=$CFGHOST --build=%{_build}
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/%{pfx}

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*

