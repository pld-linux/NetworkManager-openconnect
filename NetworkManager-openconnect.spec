Summary:	NetworkManager VPN integration for openconnect
Summary(pl.UTF-8):	Integracja NetworkManagera z openconnect
Name:		NetworkManager-openconnect
Version:	0.7.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openconnect/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	02240a490d15dd51efc701c0f6c9c425
URL:		http://projects.gnome.org/NetworkManager/
BuildRequires:	GConf2-devel
BuildRequires:	NetworkManager-devel >= 0.7.2
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.30
BuildRequires:	gettext-devel
BuildRequires:	gnome-keyring-devel
BuildRequires:	gtk+2-devel >= 2:2.8.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	NetworkManager >= 0.7.2
Requires:	openconnect
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetworkManager VPN integration for openconnect.

%description -l pl.UTF-8
Integracja NetworkManagera z openconnect.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.{a,la}

%find_lang NetworkManager-openconnect

%clean
rm -rf $RPM_BUILD_ROOT

%files -f NetworkManager-openconnect.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-openconnect-properties.so
%attr(755,root,root) %{_libdir}/nm-openconnect-service
%attr(755,root,root) %{_libdir}/nm-openconnect-service-openconnect-helper
%{_sysconfdir}/NetworkManager/VPN/nm-openconnect-service.name
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dbus-1/system.d/nm-openconnect-service.conf
%dir %{_datadir}/gnome-vpn-properties/openconnect
%{_datadir}/gnome-vpn-properties/openconnect/nm-openconnect-dialog.glade
