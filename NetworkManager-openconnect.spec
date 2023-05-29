#
# Conditional build:
%bcond_without	gtk4	# Gtk4 version of editor plugin (GNOME 42+)

Summary:	NetworkManager VPN integration for openconnect
Summary(pl.UTF-8):	Integracja NetworkManagera z openconnect
Name:		NetworkManager-openconnect
Version:	1.2.10
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/NetworkManager-openconnect/1.2/%{name}-%{version}.tar.xz
# Source0-md5:	7d814d8f8cbb024ef96818103b3c8a68
URL:		https://wiki.gnome.org/Projects/NetworkManager
BuildRequires:	NetworkManager-devel >= 2:1.2.0
BuildRequires:	NetworkManager-gtk-lib-devel >= 1.2.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gcr-ui-devel >= 3.4
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.34
BuildRequires:	gtk+3-devel >= 3.12
# with fallback to gtk-webkit4
BuildRequires:	gtk-webkit4.1-devel >= 2.36
%{?with_gtk4:BuildRequires:	gtk4-devel >= 4.0}
BuildRequires:	intltool >= 0.35.0
%{?with_gtk4:BuildRequires:	libnma-gtk4-devel >= 1.8.33}
BuildRequires:	libsecret-devel >= 0.18
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	openconnect-devel >= 3.02
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	NetworkManager >= 2:1.2.0
Requires:	gcr-ui >= 3.4
Requires:	glib2 >= 1:2.34
Requires:	gtk+3 >= 3.12
Requires:	libsecret >= 0.18
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
	--disable-static \
	%{?with_gtk4:--with-gtk4}
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
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-openconnect.so
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-vpn-plugin-openconnect-editor.so
%if %{with gtk4}
%attr(755,root,root) %{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-openconnect-editor.so
%endif
%attr(755,root,root) %{_libexecdir}/nm-openconnect-auth-dialog
%attr(755,root,root) %{_libexecdir}/nm-openconnect-service
%attr(755,root,root) %{_libexecdir}/nm-openconnect-service-openconnect-helper
%{_prefix}/lib/NetworkManager/VPN/nm-openconnect-service.name
%{_datadir}/dbus-1/system.d/nm-openconnect-service.conf
%{_datadir}/metainfo/network-manager-openconnect.metainfo.xml
