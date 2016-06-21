Summary:	NetworkManager VPN integration for openconnect
Summary(pl.UTF-8):	Integracja NetworkManagera z openconnect
Name:		NetworkManager-openconnect
Version:	1.2.2
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/NetworkManager-openconnect/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	51f5c492bb03a34b9d3015ee74972c3f
URL:		https://wiki.gnome.org/Projects/NetworkManager
BuildRequires:	NetworkManager-devel >= 2:1.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32
BuildRequires:	gtk+3-devel >= 3.4
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libsecret-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	openconnect-devel >= 3.02
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	NetworkManager >= 2:1.2.0
Requires:	glib2 >= 1:2.32
Requires:	gtk+3 >= 3.4
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
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/NetworkManager/*.la

%find_lang NetworkManager-openconnect

%clean
rm -rf $RPM_BUILD_ROOT

%files -f NetworkManager-openconnect.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-openconnect-properties.so
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-openconnect.so
%attr(755,root,root) %{_libdir}/nm-openconnect-auth-dialog
%attr(755,root,root) %{_libdir}/nm-openconnect-service
%attr(755,root,root) %{_libdir}/nm-openconnect-service-openconnect-helper
%{_prefix}/lib/NetworkManager/VPN/nm-openconnect-service.name
%{_sysconfdir}/NetworkManager/VPN/nm-openconnect-service.name
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/nm-openconnect-service.conf
%{_datadir}/appdata/network-manager-openconnect.metainfo.xml
%dir %{_datadir}/gnome-vpn-properties/openconnect
%{_datadir}/gnome-vpn-properties/openconnect/nm-openconnect-dialog.ui
