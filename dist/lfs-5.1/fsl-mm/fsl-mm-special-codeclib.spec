%define pfx /opt/freescale/rootfs/%{_target_cpu}
%define corelibpath release/lib
%define coreapppath release/exe
%define coreheaderpath ghdr
Summary         : Freescale Multimedia core libraries
Name            : fsl-mm-special-codeclib
Version         : 2.0.1
Release         : 1
License         : Freescale Proprietary
Vendor          : Freescale Semiconductor
Packager        : Dexter Ji
Group           : Applications/System
Source          : %{name}-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup

%Build

%Install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib
install -d $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin
install -d $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/include

PLATFORMSHORTNAME=`echo $PLATFORM | sed "s,imx\([0-9]*\).*,MX\1,g"`

find %{corelibpath} -name "*arm9*.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{corelibpath} -name "*arm11*.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{corelibpath} -name "*arm12*.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "*test_*" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/


if [ "x$PLATFORMSHORTNAME" = "xMX31" ]
then
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm12*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm12*.*" | xargs rm -f

elif [ "x$PLATFORMSHORTNAME" = "xMX35" ]
then
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm12*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm12*.*" | xargs rm -f

elif [ "x$PLATFORMSHORTNAME" = "xMX37" ]
then
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm12*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm12*.*" | xargs rm -f

elif [ "x$PLATFORMSHORTNAME" = "xMX51" ]
then
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_realvideo_dec_arm*_elinux.so" | xargs rm -f

elif [ "x$PLATFORMSHORTNAME" = "xMX50" ]
then
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_realvideo_dec_arm*_elinux.so" | xargs rm -f

fi

cp -rf ghdr  $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/include/mm_ghdr

install -d $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/pkgconfig/

install pkgconfig/*.pc $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/pkgconfig/


%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(777,root,root)
%{pfx}/*

