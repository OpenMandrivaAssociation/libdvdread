%define major	7
%define libname	%mklibname dvdread %{major}
%define devname	%mklibname dvdread -d

Summary:	Library to read DVD images
Name:		libdvdread
Version:	6.0.2
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.mplayerhq.hu/
Source0:	http://download.videolan.org/pub/videolan/libdvdread/%{version}/%{name}-%{version}.tar.bz2

%description
libdvdread provides a simple foundation for reading DVD-Video images.

%package -n	%{libname}
Summary:	Library to read DVD images
Group:		System/Libraries

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
%setup -q
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libdvdread.so.%{major}*

%files -n %{devname}
%doc README AUTHORS TODO
%{_includedir}/dvdread
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/dvdread.pc
%{_docdir}/libdvdread
