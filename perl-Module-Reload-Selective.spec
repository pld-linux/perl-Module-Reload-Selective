#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Reload-Sel
Summary:	Module::Reload::Selective - reload Perl modules during development
Summary(pl):	Module::Reload::Selective - prze�adowywanie modu��w Perla w trakcie pracy
Name:		perl-Module-Reload-Selective
Version:	1.02
Release:	2
# sa,e as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	27c209d6143b15d036263e31b18f6128
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Module/Reload
%{_mandir}/man3/*
