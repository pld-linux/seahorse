Summary:	SeaHorse - A Gnome front end for GnuPG
Summary(pl):	SeaHorse - frontend GNOME do GnuPG
Name:		seahorse
Version:	0.7.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.7/%{name}-%{version}.tar.bz2
URL:		http://seahorse.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gnome-mime-data-devel
BuildRequires:	gpgme-devel >= 0.3.14
BuildConflicts:	gpgme-devel >= 0.4.0
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	eel-devel
Requires(post,postun):	/usr/bin/scrollkeeper-update
Requires(post):	GConf2
Requires:	gnupg >= 1.2.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Seahorse is a Gnome front end for GnuPG - the Gnu Privacy Guard
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

%prep
%setup -q

%build
rm -f missing
intltoolize --copy --force
glib-gettextize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

# Remove useless stati file
rm $RPM_BUILD_ROOT%{_libdir}/bonobo/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/seahorse
%attr(755,root,root) %{_bindir}/seahorse-pgp-preferences
%attr(755,root,root) %{_libdir}/bonobo/*.so
%{_libdir}/bonobo/*.la
%{_libdir}/bonobo/servers/*.server
%{_sysconfdir}/gconf/schemas/*
%{_desktopdir}/*.desktop
%{_omf_dest_dir}/%{name}
%{_datadir}/%{name}
%{_datadir}/mime-info/%{name}.*
%{_datadir}/control-center-2.0/capplets/*.desktop
%{_pixmapsdir}/*
