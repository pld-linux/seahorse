Summary:	Seahorse - A GNOME front end for GnuPG
Summary(pl.UTF-8):	Seahorse - frontend GNOME do GnuPG
Name:		seahorse
Version:	2.32.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/seahorse/2.32/%{name}-%{version}.tar.bz2
# Source0-md5:	bffb5ba78efb7eae760e05d8473ee7ad
URL:		http://www.gnome.org/projects/seahorse/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	atk-devel >= 1.32
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	avahi-glib-devel >= 0.6
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gnome-keyring-devel >= 2.30.0
BuildRequires:	gnupg >= 1.4.5
BuildRequires:	gobject-introspection-devel >= 0.6.4
BuildRequires:	gpgme-devel >= 1:1.1.2
BuildRequires:	gtk+2-devel >= 2:2.18.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgnome-keyring-devel >= 2.26.0
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	pango-devel >= 1.28.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	gnupg >= 1.4.5
Requires:	gnupg2
Requires:	libcryptui = %{version}-%{release}
Requires:	rarian
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

%package -n libcryptui
Summary:	libcryptui library
Summary(pl.UTF-8):	Biblioteka libcryptui
License:	LGPL v2
Group:		X11/Libraries

%description -n libcryptui
libcryptui library.

%description -n libcryptui -l pl.UTF-8
Biblioteka libcryptui.

%package -n libcryptui-devel
Summary:	Header files for libcryptui library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcryptui
License:	LGPL v2
Group:		X11/Development/Libraries
Requires:	GConf2-devel >= 2.24.0
Requires:	gtk+2-devel >= 2:2.18.0
Requires:	libcryptui = %{version}-%{release}

%description -n libcryptui-devel
This is the package containing the header files for libcryptui
library.

%description -n libcryptui-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libcryptui.

%package -n libcryptui-apidocs
Summary:	libcryptui library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libcryptui
Group:		Documentation
Requires:	gtk-doc-common

%description -n libcryptui-apidocs
libcryptui library API documentation.

%description -n libcryptui-apidocs -l pl.UTF-8
Dokumentacja API biblioteki libcryptui.

%prep
%setup -q
sed -i s#^en@shaw## po/LINGUAS
rm po/en@shaw.po

%build
%{__glib_gettextize}
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	SSH_KEYGEN_PATH=%{_bindir}/ssh-keygen \
	SSH_PATH=%{_bindir}/ssh \
	--enable-gtk-doc \
	--enable-pgp \
	--with-html-dir=%{_gtkdocdir} \
	--disable-schemas-install \
	--disable-scrollkeeper \
	--disable-static \
	--disable-update-mime-database
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# remove internal API documentation
rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}/libseahorse

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install seahorse.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall seahorse.schemas

%postun
%update_icon_cache hicolor

%post	-n libcryptui -p /sbin/ldconfig
%postun	-n libcryptui -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/seahorse
%attr(755,root,root) %{_bindir}/seahorse-daemon
%dir %{_libdir}/seahorse
%attr(755,root,root) %{_libdir}/seahorse/seahorse-ssh-askpass
%attr(755,root,root) %{_libdir}/seahorse/xloadimage
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.gnome.seahorse.service
%{_desktopdir}/seahorse.desktop
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/*/*/*
%{_sysconfdir}/gconf/schemas/seahorse.schemas
%{_mandir}/man1/seahorse.1*
%{_mandir}/man1/seahorse-daemon.1*

%files -n libcryptui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcryptui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcryptui.so.0
%{_libdir}/girepository-1.0/CryptUI-0.0.typelib

%files -n libcryptui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcryptui.so
%{_libdir}/libcryptui.la
%{_includedir}/libcryptui
%{_pkgconfigdir}/cryptui-0.0.pc
%{_datadir}/gir-1.0/CryptUI-0.0.gir

%files -n libcryptui-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libcryptui
