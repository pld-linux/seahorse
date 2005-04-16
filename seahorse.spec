Summary:	SeaHorse - A GNOME front end for GnuPG
Summary(pl):	SeaHorse - frontend GNOME do GnuPG
Name:		seahorse
Version:	0.7.7
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/seahorse/0.7/%{name}-%{version}.tar.bz2
# Source0-md5:	e9dda6d9f4fa23da562b5edd026f8437
URL:		http://seahorse.sourceforge.net/
Patch0:		%{name}-install.patch
Patch1:		%{name}-desktop.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gedit2-devel >= 2.10.0
BuildRequires:	gettext-devel
BuildRequires:	gpgme-devel >= 1:1.0.0
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel >= 2.8.0
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.10.0
BuildRequires:	rpmbuild(macros) >= 1.197
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
Summary:        Seahorse plugin for Gedit
Summary(pl):    Wtyczka Seahorse dla Gedit
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires(post,preun):	GConf2
Requires:	gedit2 >= 2.10.0

%description -n gedit-plugin-seahorse
This plugin performs encryption operations on text.

%description -n gedit-plugin-seahorse -l pl
Wtyczka wykonuj±ca operacje szyfruj±ce na tekscie.

%package -n nautilus-extension-seahorse
Summary:	Seahorse extension for Nautilus
Summary(pl):	Rozszerzenie Seahorse dla Nautilusa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	nautilus >= 2.10.0

%description -n nautilus-extension-seahorse
Extension for signing and encrypting files.

%description -n nautilus-extension-seahorse -l pl
Rozszerzenie do podpisywania i szyfrowania plików.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__intltoolize}
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome

rm -f $RPM_BUILD_ROOT%{_libdir}/{gedit-2/plugins,nautilus/extensions-1.0}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%scrollkeeper_update_post
%gconf_schema_install seahorse.schemas
umask 022
update-mime-database %{_datadir}/mime

%preun
%gconf_schema_uninstall seahorse.schemas

%postun
/sbin/ldconfig
%scrollkeeper_update_postun
umask 022
update-mime-database %{_datadir}/mime

%post -n gedit-plugin-seahorse
%gconf_schema_install seahorse-gedit.schemas

%preun -n gedit-plugin-seahorse
%gconf_schema_uninstall seahorse-gedit.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/seahorse
%attr(755,root,root) %{_bindir}/seahorse-agent
%attr(755,root,root) %{_bindir}/seahorse-pgp-preferences
%attr(755,root,root) %{_libdir}/libseahorse-internal.so.*.*.*
%{_datadir}/mime/packages/seahorse.xml
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
%{_sysconfdir}/gconf/schemas/seahorse.schemas

%files -n gedit-plugin-seahorse
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gedit-2/plugins/libseahorse-pgp.so
%{_libdir}/gedit-2/plugins/seahorse-pgp.gedit-plugin
%{_sysconfdir}/gconf/schemas/seahorse-gedit.schemas

%files -n nautilus-extension-seahorse
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so
