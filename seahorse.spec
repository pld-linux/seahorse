Summary:	SeaHorse - A Gnome front end for GnuPG
Summary(pl):	SeaHorse - frontend GNOME do GnuPG
Name:		seahorse
Version:	0.7.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/seahorse/%{name}-%{version}.tar.gz
Patch0:		%{name}-am15.patch
Patch1:		%{name}-pixmapsdir.patch
URL:		http://seahorse.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gpgme-devel
BuildRequires:	intltool
BuildRequires:	libglade-devel
BuildRequires:	libgnomeui-devel
Requires(post,postun):	/usr/bin/scrollkeeper-update
Requires(post):	GConf2
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
#%patch0 -p1
#%patch1 -p1

%build
rm -f missing
intltoolize --copy --force
glib-gettextize --copy --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Utilities

%find_lang %{name} --with-gnome

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
%{_sysconfdir}/gconf/schemas/*
%{_datadir}/applications/*.desktop
%{_omf_dest_dir}/%{name}
%{_datadir}/%{name}
%{_pixmapsdir}/*
