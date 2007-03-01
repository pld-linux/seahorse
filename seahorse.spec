Summary:	SeaHorse - A GNOME front end for GnuPG
Summary(pl):	SeaHorse - frontend GNOME do GnuPG
Name:		seahorse
Version:	0.9.3
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/seahorse/0.9/%{name}-%{version}.tar.bz2
# Source0-md5:	f422acdc655d5e55a4adbdfb026ece07
URL:		http://seahorse.sourceforge.net/
Patch0:		%{name}-install.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-cflags.patch
Patch3:		%{name}-po.patch
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.62
BuildRequires:	gedit2-devel >= 2.14.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils >= 0.6.0
BuildRequires:	gnome-panel-devel >= 2.14.0
BuildRequires:	gpgme-devel >= 1:1.0.0
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	libnotify-devel >= 0.4.0
BuildRequires:	libsoup-devel >= 2.2.93
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.14.0
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires:	gnupg >= 1.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Seahorse is a GNOME front end for GnuPG - the Gnu Privacy Guard
program. It is a tool for secure communications and data storage. Data
encryption and digital signature creation can easily be performed
through a GUI and Key Management operations can easily be carried out
through an intuitive interface. Both English and Japanese is support
is provided.

%description -l pl
SeaHorse to frontend GNOME do programu GnuPG - Gnu Privacy Guard. Jest
to narzêdzie do bezpiecznego komunikowania i przechowywania danych.
Szyfrowanie danych i tworzenie cyfrowego podpisu mo¿e byæ ³atwo
realizowane poprzez graficzny interfejs u¿ytkownika, a zarz±dzanie
kluczami jest prowadzone przez intuicyjny interfejs.

%package -n gedit-plugin-seahorse
Summary:	Seahorse plugin for Gedit
Summary(pl):	Wtyczka Seahorse dla Gedit
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires(post,preun):	GConf2
Requires:	gedit2 >= 2.14.0

%description -n gedit-plugin-seahorse
This plugin performs encryption operations on text.

%description -n gedit-plugin-seahorse -l pl
Wtyczka wykonuj±ca operacje szyfruj±ce na tekscie.

%package -n nautilus-extension-seahorse
Summary:	Seahorse extension for Nautilus
Summary(pl):	Rozszerzenie Seahorse dla Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 2.14.0

%description -n nautilus-extension-seahorse
Extension for signing and encrypting files.

%description -n nautilus-extension-seahorse -l pl
Rozszerzenie do podpisywania i szyfrowania plików.

%package -n gnome-applet-seahorse
Summary:	Seahorse applet
Summary(pl):	Aplet Seahorse
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-panel >= 2.14.0

%description -n gnome-applet-seahorse
Seahorse applet.

%description -n gnome-applet-seahorse -l pl
Aplet Seahorse.

%package -n libcryptui
Summary:	libcryptui library
Summary(pl):	Biblioteka libcryptui
Group:		Libraries

%description -n libcryptui
libcryptui library.

%description -n libcryptui -l pl
Biblioteka libcryptui.

%package -n libcryptui-devel
Summary:	Header files for libcryptui library
Summary(pl):	Pliki nag³ówkowe biblioteki libcryptui
Group:		Development/Libraries
Requires:	libcryptui = %{version}-%{release}

%description -n libcryptui-devel
This is the package containing the header files for libcryptui library.

%description -n libcryptui-devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki libcryptui.

%package -n libcryptui-static
Summary:	Static libcryptui library
Summary(pl):	Statyczna biblioteka libcryptui
Group:		Development/Libraries
Requires:	libcryptui-devel = %{version}-%{release}

%description -n libcryptui-static
Static libcryptui library.

%description -n libcryptui-static -l pl
Statyczna biblioteka libcryptui.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__intltoolize}
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
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

%find_lang %{name} --with-gnome
%find_lang %{name}-applet --with-gnome

rm -f $RPM_BUILD_ROOT%{_libdir}/{gedit-2/plugins,nautilus/extensions-1.0}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/{gedit-2/plugins,nautilus/extensions-1.0}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post
%gconf_schema_install seahorse.schemas
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall seahorse.schemas

%postun
/sbin/ldconfig
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
%attr(755,root,root) %{_bindir}/seahorse-daemon
%attr(755,root,root) %{_bindir}/seahorse-preferences
%attr(755,root,root) %{_bindir}/seahorse-tool
%dir %{_libdir}/seahorse
%attr(755,root,root) %{_libdir}/seahorse/*
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/*
%{_desktopdir}/*.desktop
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
%exclude %{_pixmapsdir}/%{name}/*/%{name}-applet*
%{_iconsdir}/hicolor/*/*/*
%exclude %{_iconsdir}/hicolor/*/*/%{name}-applet*
%{_sysconfdir}/gconf/schemas/seahorse.schemas
%{_mandir}/man1/seahorse*

%files -n gedit-plugin-seahorse
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gedit-2/plugins/libseahorse-pgp.so
%{_libdir}/gedit-2/plugins/seahorse-pgp.gedit-plugin
%{_sysconfdir}/gconf/schemas/seahorse-gedit.schemas

%files -n nautilus-extension-seahorse
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so
%{_datadir}/mime/packages/seahorse.xml

%files -n gnome-applet-seahorse -f %{name}-applet.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/seahorse-applet
%{_libdir}/bonobo/servers/*
%{_omf_dest_dir}/%{name}-applet
%{_datadir}/gnome-2.0/ui/*
%{_pixmapsdir}/%{name}/*/%{name}-applet*
%{_iconsdir}/hicolor/*/*/%{name}-applet*

%files -n libcryptui
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcryptui.so.*.*.*

%files -n libcryptui-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcryptui.so
%{_libdir}/libcryptui.la
%{_includedir}/libcryptui
%{_pkgconfigdir}/*.pc

%files -n libcryptui-static
%defattr(644,root,root,755)
%{_libdir}/libcryptui.a
