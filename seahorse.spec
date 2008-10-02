Summary:	Seahorse - A GNOME front end for GnuPG
Summary(pl.UTF-8):	Seahorse - frontend GNOME do GnuPG
Name:		seahorse
Version:	2.24.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/seahorse/2.24/%{name}-%{version}.tar.bz2
# Source0-md5:	e8a7836c63b3a6f5b6c1311c86b7520b
URL:		http://www.gnome.org/projects/seahorse/
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	epiphany-devel >= 2.22.0
BuildRequires:	gedit2-devel >= 2.22.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gnome-panel-devel >= 2.22.0
BuildRequires:	gnupg >= 1.4.5
BuildRequires:	gpgme-devel >= 1:1.1.2
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	libtool
#BuildRequires:	nautilus-devel >= 2.22.0
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	sed >= 4.0
#BuildRequires:	xulrunner-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires(post,preun):	GConf2
Requires:	gnupg >= 1.4.5
Requires:	gnupg2
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	libxpcom.so

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

%package -n epiphany-extension-seahorse
Summary:	Seahorse extension for Epiphany
Summary(pl.UTF-8):	Rozszerzenie Seahorse dla Epiphany
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	epiphany >= 2.20.0

%description -n epiphany-extension-seahorse
Extension for encrypting text fields.

%description -n epiphany-extension-seahorse -l pl.UTF-8
Rozszerzenie do szyfrowania pól tekstowych.

%package -n gedit-plugin-seahorse
Summary:	Seahorse plugin for Gedit
Summary(pl.UTF-8):	Wtyczka Seahorse dla Gedit
Group:		X11/Applications
Requires(post,preun):	GConf2
Requires:	%{name} = %{version}-%{release}
Requires:	gedit2 >= 2.20.0

%description -n gedit-plugin-seahorse
This plugin performs encryption operations on text.

%description -n gedit-plugin-seahorse -l pl.UTF-8
Wtyczka wykonująca operacje szyfrujące na tekście.

%package -n nautilus-extension-seahorse
Summary:	Seahorse extension for Nautilus
Summary(pl.UTF-8):	Rozszerzenie Seahorse dla Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 2.20.0

%description -n nautilus-extension-seahorse
Extension for signing and encrypting files.

%description -n nautilus-extension-seahorse -l pl.UTF-8
Rozszerzenie do podpisywania i szyfrowania plików.

%package -n gnome-applet-seahorse
Summary:	Seahorse applet
Summary(pl.UTF-8):	Aplet Seahorse
Group:		X11/Applications
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-panel >= 2.20.0

%description -n gnome-applet-seahorse
Seahorse applet.

%description -n gnome-applet-seahorse -l pl.UTF-8
Aplet Seahorse.

%package -n libcryptui
Summary:	libcryptui library
Summary(pl.UTF-8):	Biblioteka libcryptui
Group:		Libraries

%description -n libcryptui
libcryptui library.

%description -n libcryptui -l pl.UTF-8
Biblioteka libcryptui.

%package -n libcryptui-devel
Summary:	Header files for libcryptui library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcryptui
Group:		Development/Libraries
Requires:	libcryptui = %{version}-%{release}

%description -n libcryptui-devel
This is the package containing the header files for libcryptui
library.

%description -n libcryptui-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki libcryptui.

%package -n libcryptui-static
Summary:	Static libcryptui library
Summary(pl.UTF-8):	Statyczna biblioteka libcryptui
Group:		Development/Libraries
Requires:	libcryptui-devel = %{version}-%{release}

%description -n libcryptui-static
Static libcryptui library.

%description -n libcryptui-static -l pl.UTF-8
Statyczna biblioteka libcryptui.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-update-mime-database \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf
#%find_lang %{name}-applet --with-gnome --with-omf

rm -f $RPM_BUILD_ROOT%{_libdir}/{epiphany/2.*/extensions,gedit-2/plugins,nautilus/extensions-2.0}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/{epiphany/2.*/extensions,gedit-2/plugins,nautilus/extensions-2.0}/*.la

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

%post -n gedit-plugin-seahorse
%gconf_schema_install seahorse-gedit.schemas

%preun -n gedit-plugin-seahorse
%gconf_schema_uninstall seahorse-gedit.schemas

%post -n nautilus-extension-seahorse
%update_mime_database

%preun -n nautilus-extension-seahorse
%update_mime_database

%post -n gnome-applet-seahorse
%scrollkeeper_update_post
%update_icon_cache hicolor

%postun -n gnome-applet-seahorse
%scrollkeeper_update_postun
%update_icon_cache hicolor

%post	-n libcryptui -p /sbin/ldconfig
%postun	-n libcryptui -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/seahorse
#%attr(755,root,root) %{_bindir}/seahorse-agent
%attr(755,root,root) %{_bindir}/seahorse-daemon
#%attr(755,root,root) %{_bindir}/seahorse-preferences
#%attr(755,root,root) %{_bindir}/seahorse-tool
%dir %{_libdir}/seahorse
%attr(755,root,root) %{_libdir}/seahorse/*
#%exclude %{_libdir}/seahorse/seahorse-applet
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
#%exclude %{_pixmapsdir}/%{name}/*/%{name}-applet*
%{_iconsdir}/hicolor/*/*/*
#%exclude %{_iconsdir}/hicolor/*/*/%{name}-applet*
%{_sysconfdir}/gconf/schemas/seahorse.schemas
%{_mandir}/man1/seahorse*

#%files -n epiphany-extension-seahorse
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/epiphany/2.*/extensions/libseahorseextension.so
#%{_libdir}/epiphany/2.*/extensions/seahorse.ephy-extension

#%files -n gedit-plugin-seahorse
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/gedit-2/plugins/libseahorse-pgp.so
#%{_libdir}/gedit-2/plugins/seahorse-pgp.gedit-plugin
#%{_sysconfdir}/gconf/schemas/seahorse-gedit.schemas

#%files -n nautilus-extension-seahorse
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/*.so
#%{_datadir}/mime/packages/seahorse.xml

#%files -n gnome-applet-seahorse -f %{name}-applet.lang
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/seahorse/seahorse-applet
#%{_libdir}/bonobo/servers/*
#%{_datadir}/gnome-2.0/ui/*
#%{_pixmapsdir}/%{name}/*/%{name}-applet*
#%{_iconsdir}/hicolor/*/*/%{name}-applet*

%files -n libcryptui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcryptui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcryptui.so.0

%files -n libcryptui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcryptui.so
%{_libdir}/libcryptui.la
%{_includedir}/libcryptui
%{_pkgconfigdir}/*.pc

%files -n libcryptui-static
%defattr(644,root,root,755)
%{_libdir}/libcryptui.a
