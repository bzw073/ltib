%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : Manufactory Update Application
Name            : uuc
Version         : 11.09.01
Release         : 1
License         : GPL
Vendor          : Freescale
Packager        : Frank Li
Group           : Development/Tools
URL             : http://xxxx
Source          : %{name}-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup 

%Build
make

%Install
rm -rf $RPM_BUILD_ROOT
make install DEST_DIR=$RPM_BUILD_ROOT/%{pfx}

%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(-,root,root)
%{pfx}/*
