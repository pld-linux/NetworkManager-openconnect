Summary:	NetworkManager VPN integration for openconnect
Summary(pl.UTF-8):	Integracja NetworkManagera z openconnect
Name:		NetworkManager-openconnect
Version:	0.8.999
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openconnect/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	0d3f70ccf9800030543c67bf3a26e1e0
URL:		http://projects.gnome.org/NetworkManager/
BuildRequires:	GConf2-devel
BuildRequires:	NetworkManager-devel >= 0.8.999
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libgnome-keyring-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	openconnect-devel >= 3.02
BuildRequires:	pkgconfig
Requires:	NetworkManager >= 0.8.999
Requires:	openconnect >= 3.02
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
%attr(755,root,root) %{_libdir}/nm-openconnect-auth-dialog
%attr(755,root,root) %{_libdir}/nm-openconnect-service
%attr(755,root,root) %{_libdir}/nm-openconnect-service-openconnect-helper
%{_sysconfdir}/NetworkManager/VPN/nm-openconnect-service.name
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/nm-openconnect-service.conf
%dir %{_datadir}/gnome-vpn-properties/openconnect
%{_datadir}/gnome-vpn-properties/openconnect/nm-openconnect-dialog.ui
