%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Reload-Sel
Summary:	Module::Reload::Selective -- Reload perl modules during development
Summary(pl):	Module::Reload::Selective -- Prze�aduj modu� perla w trakcie pracy
Name:		perl-Module-Reload-Selective
Version:	1.02
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility for module developers to selectively reload needed modules
and/or conditionally augment @INC with additional, per-developer library
directories, at development time based on environment variables.

%description -l pl
Narz�dzie dla tw�rc�w modu��w, s�u��ce do wybi�rczego prze�adowywania
modu��w i/lub warunkowego dodawania do @INC dodatkowych, specyficznych
dla konkretnego developera katalog�w z bibliotekami w trakcie pisania
programu w oparciu o zmienne �rodowiskowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}
#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Module/Reload
%{_mandir}/man3/*
