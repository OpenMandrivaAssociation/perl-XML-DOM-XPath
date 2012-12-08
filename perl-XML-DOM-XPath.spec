%define upstream_name	 XML-DOM-XPath
%define upstream_version 0.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	XPath support to XML::DOM, using XML::XPath engine
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIROD/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-XML-XPath
BuildRequires:	perl-XML-XPathEngine
BuildRequires:	perl-XML-DOM
BuildArch:	noarch
Provides:	perl-libxml-enno = %{version}-%{release}

%description
XML::DOM::XPath allows you to use XML::XPath methods to query a DOM. This is
often much easier than relying only on getElementsByTagName.

It lets you use all of the XML::DOM methods.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%check
make test

%files
%{perl_vendorlib}/XML
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.140.0-4mdv2012.0
+ Revision: 765837
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.140.0-2
+ Revision: 667415
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 564705
- BR perl-XML-DOM

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2010.1
+ Revision: 401868
- rebuild using %%perl_convert_version

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.14-2mdv2009.0
+ Revision: 265466
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.14-1mdv2009.0
+ Revision: 195077
+ rebuild (emptylog)

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.13-2mdv2008.1
+ Revision: 180651
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 08 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2007.0
+ Revision: 93773
- new version

* Tue Nov 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.12-1mdv2007.1
+ Revision: 84098
- new version
- Import perl-XML-DOM-XPath

* Wed Nov 02 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdk
- New release 0.10

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.09-3mdk
- fix deps

* Wed Jun 08 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-2mdk 
- spec cleanup
- make test in %%check
- don't ship useless empty directories

* Wed Mar 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.09-1mdk
- 0.09

* Mon Jan 17 2005 Guillaume Rousse <guillomovitch@mandrake.org> 0.06-1mdk 
- first mdk release

