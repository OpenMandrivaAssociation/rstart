Summary:	A sample implementation of a Remote Start rsh helper
Name:		rstart
Version:	1.0.6
Release:	2
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org/releases/individual/app
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros)

%description
Rstart is a simple implementation of a Remote Start client as defined in "A
Flexible Remote Execution Protocol Based on rsh". It uses rsh as its
underlying remote execution mechanism.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

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
%doc %{_mandir}/man1/rstartd.*
%doc %{_mandir}/man1/rstart.*
