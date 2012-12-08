%define major 4
%define libname %mklibname dvdread %{major}
%define develname %mklibname dvdread -d

Summary:	Library to read DVD images
Name:		libdvdread
Version:	4.2.0
Release:	2
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.mplayerhq.hu/
Source0:	http://dvdnav.mplayerhq.hu/releases/%{name}-%{version}.tar.bz2
Patch1:		libdvdread-4.1.3-m4.patch

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
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname dvdread 3 -d} < 4.2.0

%description -n	%{develname}
This is the libraries, include files and other resources you can use
to incorporate libdvdread into applications.

%prep
%setup -q
%apply_patches

%build
./autogen.sh
%configure2_5x
%make

%install
%makeinstall_std
mkdir -p %{buildroot}/%{_bindir}

%multiarch_binaries %{buildroot}%{_bindir}/dvdread-config

%files -n %{libname}
%defattr(644,root,root,755)
%doc README AUTHORS TODO
%attr(755,root,root) %{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(644,root,root,755)
%{_includedir}/dvdread
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/aclocal/dvdread.m4
%{_libdir}/pkgconfig/dvdread.pc
%attr(755,root,root) %{_bindir}/dvdread-config
%attr(755,root,root) %{multiarch_bindir}/dvdread-config


%changelog
* Wed Nov 16 2011 Götz Waschk <waschk@mandriva.org> 4.2.0-1mdv2012.0
+ Revision: 731119
- new version
- drop patch 0
- new source URL

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 4.1.3-8
+ Revision: 661678
- multiarch fixes

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 4.1.3-7
+ Revision: 660242
- mass rebuild

* Mon Nov 01 2010 Götz Waschk <waschk@mandriva.org> 4.1.3-6mdv2011.0
+ Revision: 591435
- fix m4 macro (bug #61491)

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 4.1.3-5mdv2010.1
+ Revision: 520767
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 4.1.3-4mdv2010.0
+ Revision: 425535
- rebuild

* Wed Apr 22 2009 Frederic Crozat <fcrozat@mandriva.com> 4.1.3-3mdv2009.1
+ Revision: 368636
- Fix build on cooker
- Rebuild

* Sat Nov 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.1.3-2mdv2009.1
+ Revision: 305769
- add backward compatibility patch, from mplayer svn tree, to allow dvdbackup to build

* Tue Sep 09 2008 Götz Waschk <waschk@mandriva.org> 4.1.3-1mdv2009.0
+ Revision: 282999
- version 4.1.3
- update source URL

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 4.1.3-0.r1132.4mdv2009.0
+ Revision: 278184
- fix permissions of dvdread-config

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 4.1.3-0.r1132.3mdv2009.0
+ Revision: 278179
- fix multiarch dvdread-config script

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 4.1.3-0.r1132.2mdv2009.0
+ Revision: 278146
- add missing dvdread-config
- drop tools package

* Mon Sep 01 2008 Götz Waschk <waschk@mandriva.org> 4.1.3-0.r1132.1mdv2009.0
+ Revision: 278135
- new svn snapshot
- new major
- update file list
- update license
- drop patches

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.9.7-8mdv2009.0
+ Revision: 222538
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Feb 27 2008 Götz Waschk <waschk@mandriva.org> 0.9.7-7mdv2008.1
+ Revision: 175683
- replace patch 1 with a different one

* Mon Feb 25 2008 Götz Waschk <waschk@mandriva.org> 0.9.7-6mdv2008.1
+ Revision: 174643
- fix for copy protected DVDs (bug #38118)

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.9.7-5mdv2008.1
+ Revision: 150555
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-4mdv2008.0
+ Revision: 76973
- cleanup borked deps

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-3mdv2008.0
+ Revision: 76822
- new devel naming


* Wed Jan 24 2007 Götz Waschk <waschk@mandriva.org> 0.9.7-2mdv2007.0
+ Revision: 112817
- rebuild
- Import libdvdread

* Sat Oct 07 2006 G�tz Waschk <waschk@mandriva.org> 0.9.7-1mdv2007.1
- rediff the patch
- New version 0.9.7

* Thu May 04 2006 G�tz Waschk <waschk@mandriva.org> 0.9.6-1mdk
- update the patch
- New release 0.9.6

* Mon Jan 23 2006 G�tz Waschk <waschk@mandriva.org> 0.9.5-1mdk
- update the patch
- New release 0.9.5
- use mkrel

* Mon Dec 05 2005 Götz Waschk <waschk@mandriva.org> 0.9.4-6mdk
- Rebuild

* Tue Nov 30 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.9.4-5mdk 
- patched makefile to export UDF* symbols too
- rpmbuildupdate aware

* Tue Nov 09 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.9.4-4mdk
- rebuild

* Sat Aug 14 2004 G�tz Waschk <waschk@linux-mandrake.com> 0.9.4-3mdk
- rebuild

