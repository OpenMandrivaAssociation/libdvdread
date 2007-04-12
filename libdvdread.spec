%define version 0.9.7
%define release %mkrel 2

%define name libdvdread
%define major 3
%define libname %mklibname dvdread %major

Summary:	Library to read DVD images
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		System/Libraries
Source0:	http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}.tar.bz2
#gw add UDF.* to list of exported symbols
Patch0:		libdvdread-automake.patch
URL:		http://www.dtek.chalmers.se/groups/dvd/
BuildRoot:	%_tmppath/%{name}-buildroot

%description
libdvdread provides a simple foundation for reading DVD-Video images.

%package -n %libname
Summary:	Library to read DVD images
Group:		System/Libraries

%description -n %libname
Libdvdread provides a simple foundation for reading DVD-Video images.
This package contains the shared library to run applications utilizing
libdvdread.


%package -n %libname-devel
Summary:	Libdvdread library headers
Group:		Development/C
Requires:	%{libname} = %{version}
Provides: %name-devel = %version-%release

%description -n %libname-devel
This is the libraries, include files and other resources you can use
to incorporate libdvdread into applications.

%package utils
Summary:	Libdvdread utilities
Group:		Video

%description utils
This contains some test utilities based on libdvdread: ifo_dump,
play_title and title_info.

%prep
%setup -q 
%patch -p1

%build
rm missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall
mkdir -p %buildroot/%_bindir
cp src/.libs/* %buildroot/%_bindir

%post -n %libname  -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(644,root,root,755)
%doc README AUTHORS TODO
%attr(755,root,root) %{_libdir}/lib*.so.%{major}*

%files -n %libname-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%_libdir/*.a
%{_includedir}/dvdread

%files utils
%defattr(755,root,root,755)
%_bindir/*


