%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Z160 2D driver
Name            : libz160-bin
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
This package provides proprietary driver library binary and header for Z160.

%{summary}

%Prep
%setup

%Build

%Install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{pfx}
cp -vrf * $RPM_BUILD_ROOT/%{pfx}

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(755,root,root)
%{pfx}/*
