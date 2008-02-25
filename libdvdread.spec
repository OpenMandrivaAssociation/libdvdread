%define major 3
%define libname %mklibname dvdread %{major}
%define develname %mklibname dvdread -d

Summary:	Library to read DVD images
Name:		libdvdread
Version:	0.9.7
Release:	%mkrel 6
License:	GPL
Group:		System/Libraries
URL:		http://www.dtek.chalmers.se/groups/dvd/
Source0:	http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}.tar.bz2
#gw add UDF.* to list of exported symbols
Patch0:		libdvdread-automake.patch
#gw: fix for copy protected DVDs with invalid UDF file system (bug #38118)
Patch1: http://tobias.rautenkranz.ch/code/libdvdread_udf.patch
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

%package	utils
Summary:	Libdvdread utilities
Group:		Video

%description	utils
This contains some test utilities based on libdvdread: ifo_dump,
play_title and title_info.

%prep

%setup -q 
%patch -p1
%patch1 -p1

%build
rm missing
libtoolize --copy --force; aclocal; autoconf; automake -a -c

%configure2_5x 
%make

%install
rm -rf %{buildroot}

%makeinstall
mkdir -p %{buildroot}/%{_bindir}
cp src/.libs/* %{buildroot}/%{_bindir}

%post -n %{libname}  -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

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
%{_libdir}/*.a

%files utils
%defattr(755,root,root,755)
%{_bindir}/*
