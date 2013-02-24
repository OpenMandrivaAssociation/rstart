Name: rstart
Version: 1.0.5
Release: 1
Summary: A sample implementation of a Remote Start rsh helper
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(x11)
BuildRequires: x11-util-macros >= 1.0.1

%description
Rstart is a simple implementation of a Remote Start client as defined in "A
Flexible Remote Execution Protocol Based on rsh". It uses rsh as its
underlying remote execution mechanism.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/rstartd
%{_bindir}/rstart
%{_libdir}/X11/rstart/rstartd.real
%{_libdir}/X11/rstart/config
%{_libdir}/X11/rstart/commands/@List
%{_libdir}/X11/rstart/commands/x11r6/Terminal
%{_libdir}/X11/rstart/commands/x11r6/@List
%{_libdir}/X11/rstart/commands/x11r6/LoadMonitor
%{_libdir}/X11/rstart/commands/ListGenericCommands
%{_libdir}/X11/rstart/commands/ListContexts
%{_libdir}/X11/rstart/contexts/default
%{_libdir}/X11/rstart/contexts/@List
%{_libdir}/X11/rstart/contexts/x11r6
%{_libdir}/X11/rstart/*/x11
%{_libdir}/X11/rstart/*/x
%{_mandir}/man1/rstartd.*
%{_mandir}/man1/rstart.*


%changelog
* Mon Feb 20 2012 abf
- The release updated by ABF

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2011.0
+ Revision: 669452
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 592502
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2010.1
+ Revision: 523931
- rebuilt for 2010.1

* Mon Aug 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2010.0
+ Revision: 407784
- adjust file list
- new release

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.2-6mdv2009.1
+ Revision: 351544
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-5mdv2009.0
+ Revision: 225337
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-4mdv2008.1
+ Revision: 166414
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Tue Jan 22 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-3mdv2008.1
+ Revision: 156432
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2008.0
+ Revision: 67342
- fix man pages extension


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Wed May 17 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-17 00:16:46 (27486)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

