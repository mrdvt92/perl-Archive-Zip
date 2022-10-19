Name:           perl-Archive-Zip
Version:        1.68
Release:        1%{?dist}
Summary:        Perl library for accessing Zip archives

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Archive-Zip/
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/Archive-Zip-%{version}.tar.gz
Patch0:         Archive-Zip-LICENSE-github-pr-95.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(Time::Local)
# Tests
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Test::More)
BuildRequires:  unzip
BuildRequires:  zip

Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
The Archive::Zip module allows a Perl program to create, manipulate,
read, and write Zip archive files.
Zip archives can be created, or you can read from existing zip files.
Once created, they can be written to files, streams, or strings.
Members can be added, removed, extracted, replaced, rearranged, and
enumerated.  They can also be renamed or have their dates, comments,
or other attributes queried or modified.  Their data can be compressed
or uncompressed as needed.  Members can be created from members in
existing Zip files, or from existing directories, files, or strings.


%prep
%setup -q -n Archive-Zip-%{version}
%patch0 -p1
%{__perl} -pi -e 's|^#!/bin/perl|#!%{__perl}|' examples/*.pl
%{__perl} -pi -e 's|^#!/usr/local/bin/perl|#!%{__perl}|' examples/selfex.pl


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README.md examples/
%{_bindir}/crc32
%{perl_vendorlib}/Archive/
%{_mandir}/man3/Archive*.3*


%changelog
* Web Oct 19 2022 Michael R. Davis <mrdvt@cpan.org> - 1.68-1
- Update to 1.30 - to resolve bad signature issue on zip files with large member count

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.30-11
- Mass rebuild 2013-12-27

* Wed Aug 15 2012 Daniel Mach <dmach@redhat.com> - 1.30-10.1
- Rebuild for perl 5.16

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.30-9
- Perl 5.16 rebuild
- Specify all dependencies

* Mon Mar 19 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.30-8
- 543660 apply patch from rt cpan 54827

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 1.30-6
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.30-4
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.30-3
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.30-2
- rebuild against perl 5.10.1

* Mon Jul 27 2009 Marcela Mašláňová <mmaslano@redhat.com> - 1.30-1
- update to 1.30

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 16 2008 Steven Pritchard <steve@kspei.com> 1.23-1
- Update to 1.23.

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.20-5
- Rebuild for perl 5.10 (again)

* Fri Jan 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.20-4
- rebuild for new perl

* Thu Aug 23 2007 Robin Norwood <rnorwood@redhat.com> - 1.20-3
- Fix license tag

* Wed Jun 27 2007 Robin Norwood <rnorwood@redhat.com> - 1.20-2
- Resolves: rhbz#226240
- Incorporate changes from Steven Pritchard's package review
- Fix find option order.
- Use fixperms macro instead of our own chmod incantation.
- Remove check macro cruft.
- Update build dependencies.
- Package LICENSE.
- BR unzip, zip for better test coverage.

* Tue Jun 05 2007 Robin Norwood <rnorwood@redhat.com> - 1.20-1
- Update to latest CPAN version: 1.20
- Fix broken changelog

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.16-1.2.1
- rebuild

* Fri Feb 03 2006 Jason Vas Dias<jvdias@redhat.com> - 1.16-1.2
- rebuilt for new perl-5.8.8

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Mon Jul 11 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.16-1
- Update to 1.16.

* Thu Apr 14 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.14-1
- Update to 1.14.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sun Aug 15 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.12-0.fdr.1
- Update to 1.12.

* Tue Jul  6 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.11-0.fdr.1
- Update to 1.11.
- Bring up to date with current fedora.us Perl spec template.

* Sun Apr 18 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.10-0.fdr.1
- Update to 1.10.
- Reduce directory ownership bloat.
- Require perl(:MODULE_COMPAT_*).

* Fri Nov 28 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.09-0.fdr.1
- Update to 1.09.

* Wed Oct 22 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.08-0.fdr.1
- Update to 1.08.

* Tue Oct 21 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.07-0.fdr.1
- Update to 1.07.

* Sun Sep 14 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.06-0.fdr.1
- Update to 1.06.
- Specfile cleanups.

* Sun Jun  8 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.05-0.fdr.1
- First build.
