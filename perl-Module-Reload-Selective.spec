%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Reload-Sel
Summary:	Module::Reload::Selective -- Reload perl modules during development
Summary(pl):	Module::Reload::Selective -- Prze³aduj modu³ perla w trakcie pracy
Name:		perl-Module-Reload-Selective
Version:	1.02
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	27c209d6143b15d036263e31b18f6128
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility for module developers to selectively reload needed modules
and/or conditionally augment @INC with additional, per-developer library
directories, at development time based on environment variables.

%description -l pl
Narzêdzie dla twórców modu³ów, s³u¿±ce do wybiórczego prze³adowywania
modu³ów i/lub warunkowego dodawania do @INC dodatkowych, specyficznych
dla konkretnego developera katalogów z bibliotekami w trakcie pisania
programu w oparciu o zmienne ¶rodowiskowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Module/Reload
%{_mandir}/man3/*
