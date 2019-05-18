Summary:	Seahorse - A GNOME front end for GnuPG
Summary(pl.UTF-8):	Seahorse - frontend GNOME do GnuPG
Name:		seahorse
Version:	3.32.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/seahorse/3.32/%{name}-%{version}.tar.xz
# Source0-md5:	c7dbd465f5d80c0e8f2496b71dd2e173
URL:		http://www.gnome.org/projects/seahorse/
BuildRequires:	avahi-devel >= 0.6
BuildRequires:	avahi-glib-devel >= 0.6
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gcr-devel >= 3.12.0
BuildRequires:	gcr-ui-devel >= 3.12.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gnupg2 >= 2.0.12
BuildRequires:	gpgme-devel >= 1:1.7.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libpwquality-devel
BuildRequires:	libsecret-devel >= 0.16
BuildRequires:	libsoup-devel >= 2.33.92
BuildRequires:	meson >= 0.42
BuildRequires:	ninja
BuildRequires:	openldap-devel >= 2.4.6
# ssh-keygen bin path
BuildRequires:	openssh
# ssh bin path
BuildRequires:	openssh-clients
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.727
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	vala-gcr >= 3.12.0
BuildRequires:	vala-gcr-ui >= 3.12.0
BuildRequires:	vala-libsecret >= 0.16
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	gcr >= 3.12.0
Requires:	glib2 >= 1:2.44.0
Requires:	gnome-keyring >= 3.4.0
Requires:	gnupg2 >= 2.0.12
Requires:	gpgme >= 1:1.7.0
Requires:	gtk+3 >= 3.22.0
Requires:	libsecret >= 0.16
Requires:	libsoup >= 2.33.92
Obsoletes:	gnome-keyring-manager
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Seahorse is a GNOME front end for GnuPG - the Gnu Privacy Guard
program. It is a tool for secure communications and data storage. Data
encryption and digital signature creation can easily be performed
through a GUI and Key Management operations can easily be carried out
through an intuitive interface. Both English and Japanese is support
is provided.

%description -l pl.UTF-8
Seahorse to frontend GNOME do programu GnuPG - Gnu Privacy Guard. Jest
to narzędzie do bezpiecznego komunikowania i przechowywania danych.
Szyfrowanie danych i tworzenie cyfrowego podpisu może być łatwo
realizowane poprzez graficzny interfejs użytkownika, a zarządzanie
kluczami jest prowadzone przez intuicyjny interfejs.

%prep
%setup -q

%build
%meson build \
	-Dpgp-support=true
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/seahorse
%dir %{_libexecdir}/seahorse
%attr(755,root,root) %{_libexecdir}/seahorse/ssh-askpass
%attr(755,root,root) %{_libexecdir}/seahorse/xloadimage
%{_datadir}/%{name}
%{_desktopdir}/org.gnome.seahorse.Application.desktop
%{_iconsdir}/hicolor/*x*/apps/seahorse*.png
%{_iconsdir}/hicolor/scalable/apps/org.gnome.seahorse.Application.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.seahorse.Application-symbolic.svg
%{_datadir}/metainfo/org.gnome.seahorse.Application.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.seahorse.Application.service
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.window.gschema.xml
%{_datadir}/gnome-shell/search-providers/seahorse-search-provider.ini
%{_mandir}/man1/seahorse.1*
