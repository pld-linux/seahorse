Summary:	Seahorse - A GNOME front end for GnuPG
Summary(pl.UTF-8):	Seahorse - frontend GNOME do GnuPG
Name:		seahorse
Version:	2.28.1
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/seahorse/2.28/%{name}-%{version}.tar.bz2
# Source0-md5:	c49d4d9bcfe7620081df517ab939f67b
URL:		http://www.gnome.org/projects/seahorse/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	avahi-glib-devel >= 0.6
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gnome-keyring-devel >= 2.26.0
BuildRequires:	gnupg >= 1.4.5
BuildRequires:	gpgme-devel >= 1:1.1.2
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	gnupg >= 1.4.5
Requires:	gnupg2
Requires:	libcryptui = %{version}-%{release}
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
Requires:	gtk+2-devel >= 2:2.14.0
Requires:	libcryptui = %{version}-%{release}

%description -n libcryptui-devel
This is the package containing the header files for libcryptui
library.

%description -n libcryptui-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libcryptui.

%package -n libcryptui-static
Summary:	Static libcryptui library
Summary(pl.UTF-8):	Statyczna biblioteka libcryptui
License:	LGPL v2
Group:		X11/Development/Libraries
Requires:	libcryptui-devel = %{version}-%{release}

%description -n libcryptui-static
Static libcryptui library.

%description -n libcryptui-static -l pl.UTF-8
Statyczna biblioteka libcryptui.

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
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir} \
	--disable-schemas-install \
	--disable-scrollkeeper
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
%scrollkeeper_update_post
%gconf_schema_install seahorse.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall seahorse.schemas

%postun
%scrollkeeper_update_postun
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
%{_sysconfdir}/xdg/autostart/seahorse-daemon.desktop
%{_sysconfdir}/gconf/schemas/seahorse.schemas
%{_mandir}/man1/seahorse-daemon.1*

%files -n libcryptui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcryptui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcryptui.so.0

%files -n libcryptui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcryptui.so
%{_libdir}/libcryptui.la
%{_includedir}/libcryptui
%{_pkgconfigdir}/cryptui-0.0.pc

%files -n libcryptui-static
%defattr(644,root,root,755)
%{_libdir}/libcryptui.a

%files -n libcryptui-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libcryptui
