#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	File
%define	pnam	Copy-Recursive
Summary:	File::Copy::Recursive - recursively copying files and directories
Summary(pl.UTF-8):	File::Copy::Recursive - rekurencyjne kopiowanie plików i katalogów
Name:		perl-File-Copy-Recursive
Version:	0.45
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e5eee1a3f8ae3aebbac063ea54870e54
URL:		https://metacpan.org/dist/File-Copy-Recursive
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-File-Temp
BuildRequires:	perl-Path-Tiny
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-File
BuildRequires:	perl-Test-Warnings
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module copies and moves directories recursively (or single files,
well... singley) to an optional depth and attempts to preserve each
file or directory's mode.

%description -l pl.UTF-8
Te moduł kopiuje i przenosi katalogi rekurencyjnie (lub pojedyncze
pliki... pojedynczo) do opcjonalnej głębokości i próbuje zachować
uprawnienia każdego pliku i katalogu.

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
%doc Changes README README.md
%dir %{perl_vendorlib}/File/Copy
%{perl_vendorlib}/File/Copy/Recursive.pm
%{_mandir}/man3/File::Copy::Recursive.3pm*
