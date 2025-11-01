%define major	8
%define oldlibname	%mklibname dvdread 8
%define libname	%mklibname dvdread
%define devname	%mklibname dvdread -d

Summary:	Library to read DVD images
Name:		libdvdread
Version:	7.0.0
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		https://www.mplayerhq.hu/
#Source0:	http://download.videolan.org/pub/videolan/libdvdread/%{version}/%{name}-%{version}.tar.bz2
Source0:  https://code.videolan.org/videolan/libdvdread/-/archive/%{version}/libdvdread-%{version}.tar.bz2
BuildRequires: meson

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
%meson

%build
%meson_build

%install
%meson_install

%files -n %{libname}
%{_libdir}/libdvdread.so.%{major}*

%files -n %{devname}
%doc README* AUTHORS TODO
%{_includedir}/dvdread
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/dvdread.pc
%{_docdir}/libdvdread
