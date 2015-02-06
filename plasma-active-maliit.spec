%define debug_package %nil

Name:		plasma-active-maliit
Summary:	Virtual Keyboard for plasma-active
Version:	0.2
Release:	2
License:	Nokia
Group:		Graphical desktop/KDE
Url:		http://pa.org/
Source0:	%{name}-%{version}.tar.xz
Patch0:		export-corrct-qml-path-on-64bit.patch
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(maliit-framework)

# it makes sense to require maliit-framework as this keyboard is not functional without it
Requires: maliit-framework

%description
Virtual Keyboard for plasma-active.

%prep
%setup -q
%ifarch x86_64
%patch0
%endif

%build
%qmake_qt4 PREFIX=%{_prefix} BINDIR=%{_bindir} LIBDIR=%{_libdir} INCLUDEDIR=%{_includedir}
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%files
%{_sysconfdir}/profile.d/maliitactiveinputmethod.sh
%{_libdir}/maliit
%{_datadir}/maliit
