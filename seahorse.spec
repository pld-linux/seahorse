Summary:	Seahorse - A GNOME front end for GnuPG
Summary(pl.UTF-8):	Seahorse - frontend GNOME do GnuPG
Name:		seahorse
Version:	3.20.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/seahorse/3.20/%{name}-%{version}.tar.xz
# Source0-md5:	06cdf9805d9d1adddd0140d13f1bd234
URL:		http://www.gnome.org/projects/seahorse/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	avahi-devel >= 0.6
BuildRequires:	avahi-glib-devel >= 0.6
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gcr-devel >= 3.12.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnupg2 >= 2.0.12
BuildRequires:	gpgme-devel >= 1:1.1.2
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libsecret-devel >= 0.16
BuildRequires:	libsoup-devel >= 2.33.92
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	vala-gcr >= 3.12.0
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	gcr >= 3.12.0
Requires:	gnome-keyring >= 3.4.0
Requires:	gnupg2 >= 2.0.12
Requires:	gpgme >= 1:1.1.2
Requires:	gtk+3 >= 3.4.0
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
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	SSH_KEYGEN_PATH=%{_bindir}/ssh-keygen \
	SSH_PATH=%{_bindir}/ssh \
	--enable-pgp \
	--disable-silent-rules \
	--disable-schemas-compile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/seahorse
%dir %{_libdir}/seahorse
%attr(755,root,root) %{_libdir}/seahorse/seahorse-ssh-askpass
%attr(755,root,root) %{_libdir}/seahorse/xloadimage
%{_datadir}/%{name}
%{_desktopdir}/seahorse.desktop
%{_iconsdir}/hicolor/*x*/apps/seahorse*.png
%{_iconsdir}/hicolor/symbolic/apps/seahorse-symbolic.svg
%{_datadir}/appdata/seahorse.appdata.xml
%{_datadir}/GConf/gsettings/org.gnome.seahorse.convert
%{_datadir}/GConf/gsettings/org.gnome.seahorse.manager.convert
%{_datadir}/dbus-1/services/org.gnome.seahorse.Application.service
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.window.gschema.xml
%{_datadir}/gnome-shell/search-providers/seahorse-search-provider.ini
%{_mandir}/man1/seahorse.1*
