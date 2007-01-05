Summary:	Seahorse - A GNOME front end for GnuPG
Summary(pl):	Seahorse - frontend GNOME do GnuPG
Name:		seahorse
Version:	0.9.10
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/seahorse/0.9/%{name}-%{version}.tar.bz2
# Source0-md5:	2e48cd0a1573cd417d85a5c5c69902f0
URL:		http://www.gnome.org/projects/seahorse/
Patch0:		%{name}-install.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-cflags.patch
BuildRequires:	GConf2-devel >= 2.16.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	epiphany-devel >= 2.16.1
BuildRequires:	gedit2-devel >= 2.16.2
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils >= 0.7.2
BuildRequires:	gnome-panel-devel >= 2.16.2
BuildRequires:	gpgme-devel >= 1:1.1.2
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 1:2.6.0
BuildRequires:	libgnomeui-devel >= 2.16.1
BuildRequires:	libnotify-devel >= 0.4.2
BuildRequires:	libsoup-devel >= 2.2.98
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.16.3
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires:	gnupg >= 1.4.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Seahorse is a GNOME front end for GnuPG - the Gnu Privacy Guard
program. It is a tool for secure communications and data storage. Data
encryption and digital signature creation can easily be performed
through a GUI and Key Management operations can easily be carried out
through an intuitive interface. Both English and Japanese is support
is provided.

%description -l pl
Seahorse to frontend GNOME do programu GnuPG - Gnu Privacy Guard. Jest
to narzêdzie do bezpiecznego komunikowania i przechowywania danych.
Szyfrowanie danych i tworzenie cyfrowego podpisu mo¿e byæ ³atwo
realizowane poprzez graficzny interfejs u¿ytkownika, a zarz±dzanie
kluczami jest prowadzone przez intuicyjny interfejs.

%package -n epiphany-extension-seahorse
Summary:	Seahorse extension for Epiphany
Summary(pl):	Rozszerzenie Seahorse dla Epiphany
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	epiphany >= 2.16.1

%description -n epiphany-extension-seahorse
Extension for encrypting text fields.

%description -n epiphany-extension-seahorse -l pl
Rozszerzenie do szyfrowania pól tekstowych.

%package -n gedit-plugin-seahorse
Summary:	Seahorse plugin for Gedit
Summary(pl):	Wtyczka Seahorse dla Gedit
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires(post,preun):	GConf2
Requires:	gedit2 >= 2.16.2

%description -n gedit-plugin-seahorse
This plugin performs encryption operations on text.

%description -n gedit-plugin-seahorse -l pl
Wtyczka wykonuj±ca operacje szyfruj±ce na tek¶cie.

%package -n nautilus-extension-seahorse
Summary:	Seahorse extension for Nautilus
Summary(pl):	Rozszerzenie Seahorse dla Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 2.16.3

%description -n nautilus-extension-seahorse
Extension for signing and encrypting files.

%description -n nautilus-extension-seahorse -l pl
Rozszerzenie do podpisywania i szyfrowania plików.

%package -n gnome-applet-seahorse
Summary:	Seahorse applet
Summary(pl):	Aplet Seahorse
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-panel >= 2.16.2
Requires(post,postun):	hicolor-icon-theme

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

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
CPPFLAGS="-DGPG_MAJOR=\"1\" -DGPG_MINOR=\"4\"" 
%configure \
	--disable-schemas-install \
	--disable-update-mime-database \
	--disable-gpg-check \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome
%find_lang %{name}-applet --with-gnome

rm -f $RPM_BUILD_ROOT%{_libdir}/{epiphany/2.16/extensions,gedit-2/plugins,nautilus/extensions-1.0}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/{epiphany/2.16/extensions,gedit-2/plugins,nautilus/extensions-1.0}/*.la

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
%attr(755,root,root) %{_bindir}/seahorse-agent
%attr(755,root,root) %{_bindir}/seahorse-daemon
%attr(755,root,root) %{_bindir}/seahorse-preferences
%attr(755,root,root) %{_bindir}/seahorse-tool
%dir %{_libdir}/seahorse
%attr(755,root,root) %{_libdir}/seahorse/*
%exclude %{_libdir}/seahorse/seahorse-applet
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

%files -n epiphany-extension-seahorse
%attr(755,root,root) %{_libdir}/epiphany/2.16/extensions/libseahorseextension.so
%{_libdir}/epiphany/2.16/extensions/seahorse.ephy-extension

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
%attr(755,root,root) %{_libdir}/seahorse/seahorse-applet
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
