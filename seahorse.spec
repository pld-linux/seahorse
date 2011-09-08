Summary:	Seahorse - A GNOME front end for GnuPG
Summary(pl.UTF-8):	Seahorse - frontend GNOME do GnuPG
Name:		seahorse
Version:	3.1.91
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/seahorse/3.1/%{name}-%{version}.tar.xz
# Source0-md5:	f20afeb4b2e85b29adf74244046d3315
URL:		http://www.gnome.org/projects/seahorse/
BuildRequires:	atk-devel >= 1.32
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	avahi-glib-devel >= 0.6
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gnome-keyring-devel >= 3.0.0
BuildRequires:	gnupg >= 1.4.5
BuildRequires:	gobject-introspection-devel >= 0.6.4
BuildRequires:	gpgme-devel >= 1:1.1.2
BuildRequires:	gtk+3-devel >= 3.0.0
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
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	gnupg >= 1.4.5
Requires:	gnupg2
Requires:	gnome-keyring >= 3.1.91
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
	--disable-schemas-compile \
	--disable-scrollkeeper \
	--disable-static \
	--disable-update-mime-database
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

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
%{_pixmapsdir}/*
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/GConf/gsettings/org.gnome.seahorse.convert
%{_datadir}/GConf/gsettings/org.gnome.seahorse.manager.convert
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.manager.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.seahorse.window.gschema.xml
%{_mandir}/man1/seahorse.1*
