%define pfx /opt/freescale/rootfs/%{_target_cpu}

Summary         : GPU on imx6q that supports OpenGLES and OpenVG
Name            : gpu-viv-src
Version         : 11.09.01
Release         : 1
License         : Proprietary
Vendor          : Vivante
Packager        : Richard Zhao
Group           : Development/Libraries
Source          : %{name}-%{version}.tar.gz
BuildRoot       : %{_tmppath}/%{name}
Prefix          : %{pfx}

%Description
%{summary}

%Prep
%setup

%Build

cd driver && ./driver_build_sample.sh clean && ./driver_build_sample.sh
cd ../test && ./test_build_sample.sh

%Install
SOC=$(echo $PLATFORM | cut -d_ -f1 | cut -c2-)
OUTPUT_PKG="gpu-viv-bin-$SOC-%{version}"

rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{pfx}

install -d $RPM_BUILD_ROOT/%{pfx}/usr/lib
cp -af driver/build/sdk/drivers/*.so* $RPM_BUILD_ROOT/%{pfx}/usr/lib

install -d $RPM_BUILD_ROOT/%{pfx}/opt/viv_samples
cp -af driver/build/sdk/samples/* $RPM_BUILD_ROOT/%{pfx}/opt/viv_samples/
cp -af test/build/sdk/samples/* $RPM_BUILD_ROOT/%{pfx}/opt/viv_samples/

install -d $RPM_BUILD_ROOT/%{pfx}/usr/include/
cp -af driver/build/sdk/include/* $RPM_BUILD_ROOT/%{pfx}/usr/include

# Package up the build results and leave in rpm/SOURCES
rm -rf $OUTPUT_PKG
install -d $OUTPUT_PKG
mv $RPM_BUILD_ROOT/%{pfx}/* $OUTPUT_PKG
tar -zcf $OUTPUT_PKG.tar.gz $OUTPUT_PKG
# todo fix this to use rpmdir or something better than TOP:
install $OUTPUT_PKG.tar.gz $TOP/rpm/RPMS/"$LINTARCH"
install $OUTPUT_PKG.tar.gz $TOP/rpm/SOURCES

# Now delete everything we just tarred up.
rm -rf $RPM_BUILD_ROOT/%{pfx}
# Create an empty directory for rpm to have something install or it won't be happy.
install -d $RPM_BUILD_ROOT/%{pfx}/usr

%Clean
rm -rf $RPM_BUILD_ROOT


%Files
%defattr(-,root,root)
%{pfx}/*
