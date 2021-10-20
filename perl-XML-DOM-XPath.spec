%define modname	XML-DOM-XPath
%define modver	0.14

Summary:	XPath support to XML::DOM, using XML::XPath engine
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	17
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIROD/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	perl-devel
BuildRequires:	perl-XML-XPath
BuildRequires:	perl-XML-XPathEngine
BuildRequires:	perl-XML-DOM
Provides:	perl-libxml-enno = %{version}-%{release}

%description
XML::DOM::XPath allows you to use XML::XPath methods to query a DOM. This is
often much easier than relying only on getElementsByTagName.

It lets you use all of the XML::DOM methods.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%{perl_vendorlib}/XML
%doc %{_mandir}/man3/*
