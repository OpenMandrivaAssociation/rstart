Name: rstart
Version: 1.0.2
Release: %mkrel 2
Summary: A sample implementation of a Remote Start rsh helper
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
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
%{_mandir}/man1/rstartd.*
%{_mandir}/man1/rstart.*


