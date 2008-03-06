%define module	XML-DOM-XPath
%define version	0.13
%define release	%mkrel 2

Summary:	XPath support to XML::DOM, using XML::XPath engine
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIROD/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl-XML-XPath >= 1.13-5mdk
BuildRequires:	perl-XML-XPathEngine
Provides:	perl-libxml-enno
Obsoletes:	perl-libxml-enno
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
XML::DOM::XPath allows you to use XML::XPath methods to query a DOM. This is
often much easier than relying only on getElementsByTagName.

It lets you use all of the XML::DOM methods.

%prep

%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean 
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%{perl_vendorlib}/XML
%{_mandir}/*/*


