%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Z160 2D driver
Name            : libz160
Version         : 11.09.01
Release         : 1
License         : Proprietary
Vendor          : Freescale
Packager        : Rob Herring
Group           : System/Servers
Source          : %{name}-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
This package provides proprietary driver library for Z160.

%{summary}

%Prep
%setup

%Build
make -j1
make VERSION=%{version} pkg-bin 

%Install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT/%{pfx}/%{_prefix} install
install %{name}-bin-%{version}.tar.gz $TOP/rpm/RPMS/"$LINTARCH"
install %{name}-bin-%{version}.tar.gz $TOP/rpm/SOURCES

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(755,root,root)
%{pfx}/*
