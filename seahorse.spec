Prefix: /usr

Summary: SeaHorse - A Gnome front end for GnuPG 
Name: seahorse
Version: 0.4.0
Release: 1
Group: X11/Applications
Copyright: GPL
Source: http://seahorse.sourceforge.net/%{name}-%{version}.tar.gz
Source1: http://seahorse.sourceforge.net/%{name}-%{version}.tar.gz.sig
URL: http://seahorse.sourceforge.net/
# URL1: http://www1.kcn.ne.jp/~anthony/seahorse/
Packager: CW Zuckschwerdt <zany@triq.net>
BuildRoot: /var/tmp/%{name}-%{version}-root

%description
 Seahorse is a Gnome front end for GnuPG - the Gnu Privacy Guard program.
 It is a tool for secure communications and data storage.
 Data encryption and digital signature creation can easily be
 performed through a GUI and Key Management operations can easily be
 carried out through an intuitive interface.
 Both English and Japanese is  support is provided.

%prep

if type gpg
then

 if gpg --list-keys 61CA8871
 then
  gpg --verify ../SOURCES/%{name}-%{version}.tar.gz.sig
 else
  echo You dont have the authors key. Please try
  echo gpg --recv-keys --keyserver wwwkeys.pgp.net   61CA8871
 fi

else
 echo GPG is required
fi

%setup -n %{name}-%{version}

# %patch

%build
./configure --prefix=%{prefix}
make

%install

make DESTDIR=$RPM_BUILD_ROOT install
cd po
make prefix=$RPM_BUILD_ROOT%{prefix} install
cd ..

find $RPM_BUILD_ROOT -type f |sed -e "s+$RPM_BUILD_ROOT++" >filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f filelist
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog NEWS README

# %{prefix}/bin/seahorse
# %{prefix}/man/man?/*
# %{prefix}/share/locale/*/LC_MESSAGES/*
# %{prefix}/share/gnome/apps/Applications/*
# %{prefix}/share/pixmaps/seahorse/*
