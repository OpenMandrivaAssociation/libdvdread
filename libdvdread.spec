%define major 4
%define libname %mklibname dvdread %{major}
%define develname %mklibname dvdread -d

Summary:	Library to read DVD images
Name:		libdvdread
Version:	4.2.0
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.mplayerhq.hu/
Source0:	http://dvdnav.mplayerhq.hu/releases/%{name}-%{version}.tar.bz2
Patch1:	    libdvdread-4.1.3-m4.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
libdvdread provides a simple foundation for reading DVD-Video images.

%package -n	%{libname}
Summary:	Library to read DVD images
Group:		System/Libraries

%description -n	%{libname}
Libdvdread provides a simple foundation for reading DVD-Video images.
This package contains the shared library to run applications utilizing
libdvdread.

%package -n	%{develname}
Summary:	Libdvdread library headers
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:      %{mklibname dvdread 3 -d}

%description -n	%{develname}
This is the libraries, include files and other resources you can use
to incorporate libdvdread into applications.

%prep

%setup -q -n %name-%version
%apply_patches
./autogen.sh

%build
%configure2_5x 
%make

%install
rm -rf %{buildroot}

%makeinstall_std
mkdir -p %{buildroot}/%{_bindir}

%multiarch_binaries %{buildroot}%{_bindir}/dvdread-config

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(644,root,root,755)
%doc README AUTHORS TODO
%attr(755,root,root) %{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(644,root,root,755)
%{_includedir}/dvdread
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%_datadir/aclocal/dvdread.m4
%_libdir/pkgconfig/dvdread.pc
%attr(755,root,root) %_bindir/dvdread-config
%attr(755,root,root) %{multiarch_bindir}/dvdread-config
