#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : lcms2
Version  : 2.13.1
Release  : 22
URL      : https://github.com/mm2/Little-CMS/releases/download/lcms2.13.1/lcms2-2.13.1.tar.gz
Source0  : https://github.com/mm2/Little-CMS/releases/download/lcms2.13.1/lcms2-2.13.1.tar.gz
Summary  : LCMS Color Management Library
Group    : Development/Tools
License  : GPL-3.0 IJG MIT
Requires: lcms2-bin = %{version}-%{release}
Requires: lcms2-filemap = %{version}-%{release}
Requires: lcms2-lib = %{version}-%{release}
Requires: lcms2-license = %{version}-%{release}
Requires: lcms2-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libjpeg-turbo-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : tiff-dev
BuildRequires : zlib-dev

%description
About Little CMS
Little CMS intends to be an OPEN SOURCE small-footprint color management engine, with special focus on accuracy and performance. It uses the International Color Consortium standard (ICC), which is the modern standard when regarding to color management. The ICC specification is widely used and is referred to in many International and other de-facto standards. It was approved as an International Standard, ISO 15076-1, in 2005.

%package bin
Summary: bin components for the lcms2 package.
Group: Binaries
Requires: lcms2-license = %{version}-%{release}
Requires: lcms2-filemap = %{version}-%{release}

%description bin
bin components for the lcms2 package.


%package dev
Summary: dev components for the lcms2 package.
Group: Development
Requires: lcms2-lib = %{version}-%{release}
Requires: lcms2-bin = %{version}-%{release}
Provides: lcms2-devel = %{version}-%{release}
Requires: lcms2 = %{version}-%{release}

%description dev
dev components for the lcms2 package.


%package dev32
Summary: dev32 components for the lcms2 package.
Group: Default
Requires: lcms2-lib32 = %{version}-%{release}
Requires: lcms2-bin = %{version}-%{release}
Requires: lcms2-dev = %{version}-%{release}

%description dev32
dev32 components for the lcms2 package.


%package filemap
Summary: filemap components for the lcms2 package.
Group: Default

%description filemap
filemap components for the lcms2 package.


%package lib
Summary: lib components for the lcms2 package.
Group: Libraries
Requires: lcms2-license = %{version}-%{release}
Requires: lcms2-filemap = %{version}-%{release}

%description lib
lib components for the lcms2 package.


%package lib32
Summary: lib32 components for the lcms2 package.
Group: Default
Requires: lcms2-license = %{version}-%{release}

%description lib32
lib32 components for the lcms2 package.


%package license
Summary: license components for the lcms2 package.
Group: Default

%description license
license components for the lcms2 package.


%package man
Summary: man components for the lcms2 package.
Group: Default

%description man
man components for the lcms2 package.


%prep
%setup -q -n lcms2-2.13.1
cd %{_builddir}/lcms2-2.13.1
pushd ..
cp -a lcms2-2.13.1 build32
popd
pushd ..
cp -a lcms2-2.13.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657062582
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mprefer-vector-width=256 "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1657062582
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lcms2
cp %{_builddir}/lcms2-2.13.1/COPYING %{buildroot}/usr/share/package-licenses/lcms2/9baf05cabbfd71f06534e5597170a2b7c817e6ad
cp %{_builddir}/lcms2-2.13.1/plugins/fast_float/COPYING.GPL3 %{buildroot}/usr/share/package-licenses/lcms2/1de7bacb4fbbd7b6d391a69abfe174c2509ec303
cp %{_builddir}/lcms2-2.13.1/utils/jpgicc/LICENSE_iccjpeg %{buildroot}/usr/share/package-licenses/lcms2/0ff27b2ad965b91dda6bd751b541edd707f56fbd
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jpgicc
/usr/bin/linkicc
/usr/bin/psicc
/usr/bin/tificc
/usr/bin/transicc
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/lcms2.h
/usr/include/lcms2_plugin.h
/usr/lib64/glibc-hwcaps/x86-64-v3/liblcms2.so
/usr/lib64/liblcms2.so
/usr/lib64/pkgconfig/lcms2.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/liblcms2.so
/usr/lib32/pkgconfig/32lcms2.pc
/usr/lib32/pkgconfig/lcms2.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-lcms2

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/liblcms2.so.2
/usr/lib64/glibc-hwcaps/x86-64-v3/liblcms2.so.2.0.13
/usr/lib64/liblcms2.so.2
/usr/lib64/liblcms2.so.2.0.13

%files lib32
%defattr(-,root,root,-)
/usr/lib32/liblcms2.so.2
/usr/lib32/liblcms2.so.2.0.13

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lcms2/0ff27b2ad965b91dda6bd751b541edd707f56fbd
/usr/share/package-licenses/lcms2/1de7bacb4fbbd7b6d391a69abfe174c2509ec303
/usr/share/package-licenses/lcms2/9baf05cabbfd71f06534e5597170a2b7c817e6ad

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/jpgicc.1
/usr/share/man/man1/linkicc.1
/usr/share/man/man1/psicc.1
/usr/share/man/man1/tificc.1
/usr/share/man/man1/transicc.1
