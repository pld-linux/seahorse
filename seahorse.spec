Summary:	SeaHorse - A Gnome front end for GnuPG
Summary(pl):	SeaHorse - frontend GNOME do GnuPG
Name:		seahorse
Version:	0.5.0
Release:	3
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Source0:	ftp://download.sourceforge.net/pub/sourceforge/seahorse/%{name}-%{version}.tar.gz
URL:		http://seahorse.sourceforge.net/
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Seahorse is a Gnome front end for GnuPG - the Gnu Privacy Guard
program. It is a tool for secure communications and data storage. Data
encryption and digital signature creation can easily be performed
through a GUI and Key Management operations can easily be carried out
through an intuitive interface. Both English and Japanese is support
is provided.

%description -l pl
SeaHorse to frontend GNOME do programu GnuPG - Gnu Privacy Guard. Jest
to narz�dzie do bezpiecznego komunikowania i przechowywania danych.
Szyfrowanie danych i tworzenie cyfrowego podpisu mo�e by� �atwo
realizowane poprzez graficzny interfejs u�ytkownika, a zarz�dzanie
kluczami jest prowadzone przez intuicyjny interfejs.

%prep
%setup -q

%build
gettextize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Utilities

gzip -9nf AUTHORS ChangeLog NEWS README

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz

%attr(755,root,root) %{_bindir}/seahorse
%{_mandir}/man?/*
%{_applnkdir}/Utilities/*
%{_pixmapsdir}/seahorse
