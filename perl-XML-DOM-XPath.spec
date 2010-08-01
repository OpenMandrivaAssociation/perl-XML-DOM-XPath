%define upstream_name	 XML-DOM-XPath
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	XPath support to XML::DOM, using XML::XPath engine
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIROD/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildRequires:	perl-XML-XPath >= 1.13-5mdk
BuildRequires:	perl-XML-XPathEngine
BuildRequires:	perl-XML-DOM
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Provides:	perl-libxml-enno
Obsoletes:	perl-libxml-enno

%description
XML::DOM::XPath allows you to use XML::XPath methods to query a DOM. This is
often much easier than relying only on getElementsByTagName.

It lets you use all of the XML::DOM methods.

%prep

%setup -q -n %{upstream_name}-%{upstream_version}

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
