%define pfx /opt/freescale/rootfs/%{_target_cpu}
%define corelibpath release/lib
%define coreapppath release/exe
%define coreheaderpath ghdr
%define coreconfpath etc
Summary         : Freescale Multimedia Microsoft core libraries
Name            : fsl-mm-aacpenc-codeclib
Version         : 2.0.0
Release         : 1
License         : Freescale Proprietary
Vendor          : Freescale
Packager        : Lyon Wang
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
mkdir -p $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib
mkdir -p $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin
mkdir -p $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/include
mkdir -p $RPM_BUILD_ROOT/%{pfx}/etc

PLATFORMSHORTNAME=`echo $PLATFORM | sed "s,imx\([0-9]*\).*,MX\1,g"`

find %{corelibpath} -name "*arm9*.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{corelibpath} -name "*arm11*.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{corelibpath} -name "*arm12*.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "*test_*" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
find %{coreconfpath} -name "*asound.conf*" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/etc/

if [ "x$PLATFORMSHORTNAME" = "xMX25" ]
then
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm12*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm11*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_deinterlace_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm11*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm12*.*" | xargs rm -f
elif [ "x$PLATFORMSHORTNAME" = "xMX233" ]
then
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm12*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm11*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_deinterlace_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm11*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm12*.*" | xargs rm -f
elif [ "x$PLATFORMSHORTNAME" = "xMX27" ]
then
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm12*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm11*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_deinterlace_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm11*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm12*.*" | xargs rm -f
elif [ "x$PLATFORMSHORTNAME" = "xMX31" ]
then
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm12*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_deinterlace_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm12*.*" | xargs rm -f
find %{corelibpath} -name "lib_wb_amr_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_wb_amr_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
find %{corelibpath} -name "lib_nb_amr_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_nb_amr_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
find %{corelibpath} -name "lib_g.729ab_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_g.729ab_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
find %{corelibpath} -name "lib_g.723.1_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_g.723.1_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
elif [ "x$PLATFORMSHORTNAME" = "xMX35" ]
then
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm12*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_deinterlace_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "libmpeg4_encoder_arm11_ELINUX.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm12*.*" | xargs rm -f
find %{corelibpath} -name "lib_wb_amr_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_wb_amr_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
find %{corelibpath} -name "lib_nb_amr_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_nb_amr_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
find %{corelibpath} -name "lib_g.729ab_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_g.729ab_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
find %{corelibpath} -name "lib_g.723.1_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_g.723.1_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
elif [ "x$PLATFORMSHORTNAME" = "xMX37" ]
then
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm12*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_H264_dec_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_mpeg2_dec_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_MPEG4_dec_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_MPEG4ASP_dec_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_WMV9MP_dec_MP_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "libmpeg4_encoder_arm11_ELINUX.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm12*.*" | xargs rm -f
find %{corelibpath} -name "lib_wb_amr_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_wb_amr_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
find %{corelibpath} -name "lib_nb_amr_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_nb_amr_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
find %{corelibpath} -name "lib_g.729ab_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_g.729ab_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
find %{corelibpath} -name "lib_g.723.1_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_g.723.1_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
elif [ "x$PLATFORMSHORTNAME" = "xMX51" ]
then
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_H264_dec_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_mpeg2_dec_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_MPEG4_dec_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_MPEG4ASP_dec_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_WMV9MP_dec_MP_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_wma10_dec_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_mp3_dec_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_aac_dec_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "libmpeg4_encoder_arm11_ELINUX.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_mp3_enc_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm9*.*" | xargs rm -f
find %{corelibpath} -name "lib_nb_amr_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_nb_amr_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
find %{corelibpath} -name "lib_g.729ab_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_g.729ab_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
find %{corelibpath} -name "lib_g.723.1_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_g.723.1_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
elif [ "x$PLATFORMSHORTNAME" = "xMX50" ]
then
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "*arm9*.*" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_wma10_dec_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_mp3_dec_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_aac_dec_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "libmpeg4_encoder_arm11_ELINUX.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/ -name "lib_mp3_enc_arm11_elinux.so" | xargs rm -f
find $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/ -name "test*arm9*.*" | xargs rm -f
find %{corelibpath} -name "lib_nb_amr_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_nb_amr_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
find %{corelibpath} -name "lib_g.729ab_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_g.729ab_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
find %{corelibpath} -name "lib_g.723.1_*_arm9_elinux.so" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/
find %{coreapppath} -name "test_g.723.1_*_arm9_elinux" | xargs -I corelib install corelib $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/bin/
fi

cp -r ghdr $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/include/mm_ghdr
mkdir -p $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/pkgconfig/

cp pkgconfig/*.pc $RPM_BUILD_ROOT/%{pfx}/%{_prefix}/lib/pkgconfig/


%Clean
rm -rf $RPM_BUILD_ROOT

%Files
%defattr(777,root,root)
%{pfx}/*

