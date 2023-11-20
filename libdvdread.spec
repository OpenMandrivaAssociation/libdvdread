%define major	8
%define oldlibname	%mklibname dvdread 8
%define libname	%mklibname dvdread
%define devname	%mklibname dvdread -d

Summary:	Library to read DVD images
Name:		libdvdread
Version:	6.1.3
Release:	3
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.mplayerhq.hu/
Source0:	http://download.videolan.org/pub/videolan/libdvdread/%{version}/%{name}-%{version}.tar.bz2

%description
libdvdread provides a simple foundation for reading DVD-Video images.

%package -n	%{libname}
Summary:	Library to read DVD images
Group:		System/Libraries
%rename %{oldlibname}

%description -n	%{libname}
Libdvdread provides a simple foundation for reading DVD-Video images.
This package contains the shared library to run applications utilizing
libdvdread.

%package -n	%{devname}
Summary:	Libdvdread library headers
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This is the libraries, include files and other resources you can use
to incorporate libdvdread into applications.

%prep
%autosetup -p1
%configure
# ****ing libtool strips out -mllvm options passed to the linker,
# so we have to try harder to convince it
sed -i -e 's|-shared \\|-shared -Wl,-mllvm,-instcombine-infinite-loop-threshold=1000 \\|g' libtool

%build
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libdvdread.so.%{major}*

%files -n %{devname}
%doc README* AUTHORS TODO
%{_includedir}/dvdread
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/dvdread.pc
%{_docdir}/libdvdread
