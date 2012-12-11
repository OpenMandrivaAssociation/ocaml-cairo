# There are no source releases for ocaml-cairo.  To get the source
# matching this you have to do:
#
# cvs -d:pserver:anonymous@cvs.cairographics.org:/cvs/cairo co -D 2008-03-01 cairo-ocaml
# tar zcf /tmp/ocaml-cairo-1.2.0.cvs20080301.tar.gz --exclude CVS cairo-ocaml
#
# Whether you'll get precisely the same tarball by this method is
# questionable.  If files get checked out in a different order then
# you might need to use 'diff -urN' instead of comparing MD5 hashes.

# Using git:
# $ git clone git://anongit.freedesktop.org/cairo-ocaml
# $ git archive --format=tar --prefix=cairo-ocaml/ cairo-ocaml-1.2.0 | gzip > ocaml-cairo-1.2.0.tar.gz


Name:           ocaml-cairo
Version:        1.2.0.1
Release:        5

Summary:        OCaml library for accessing cairo graphics
Group:          Development/Other
License:        LGPLv2

URL:            http://cairographics.org/cairo-ocaml/
Source0:        ocaml-cairo-%{version}.tar.gz
Source1:        ocaml-cairo-META
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

Requires:       ocaml
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lablgtk2-devel
BuildRequires:  cairo-devel
BuildRequires:  automake
BuildRequires:  gtk2-devel
BuildRequires:  chrpath

%description
Cairo is a multi-platform library providing anti-aliased vector-based
rendering for multiple target backends. Paths consist of line segments
and cubic splines and can be rendered at any width with various join
and cap styles. All colors may be specified with optional translucence
(opacity/alpha) and combined using the extended Porter/Duff
compositing algebra as found in the X Render Extension.

Cairo exports a stateful rendering API similar in spirit to the path
construction, text, and painting operators of PostScript, (with the
significant addition of translucence in the imaging model). When
complete, the API is intended to support the complete imaging model of
PDF 1.4.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n cairo-ocaml
aclocal -I support
autoconf
%configure2_5x
cp %{SOURCE1} META

%build
make
make doc
sed -i -e 's:@VERSION@:%{version}:g' META

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs

ocamlfind install cairo src/{*.mli,*.cmi,*.cma,*.a,*.cmxa,*.cmx,dll*.so} META

strip %{buildroot}%{_libdir}/ocaml/stublibs/dll*.so
chrpath --delete %{buildroot}%{_libdir}/ocaml/stublibs/dll*.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/ocaml/cairo
%exclude %{_libdir}/ocaml/cairo/*.a
%exclude %{_libdir}/ocaml/cairo/*.cmxa
%exclude %{_libdir}/ocaml/cairo/*.cmx
%exclude %{_libdir}/ocaml/cairo/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner

%files devel
%defattr(-,root,root,-)
%doc COPYING ChangeLog README doc/html
%{_libdir}/ocaml/cairo/*.a
%{_libdir}/ocaml/cairo/*.cmxa
%{_libdir}/ocaml/cairo/*.cmx
%{_libdir}/ocaml/cairo/*.mli



%changelog
* Mon Sep 19 2011 Alexandre Lissy <alissy@mandriva.com> 1.2.0.1-5
+ Revision: 700302
- Changing BuildRequires against ocaml-lablgtk2 to -devel
- Updating version
- Release bump
- Using tarball from git, not cvs
  Updating BuildRequires against ocaml-lablgtk2 instead of ocaml-lablgtk2-devel because of pango.cmo needed

* Thu Apr 22 2010 Florent Monnier <blue_prawn@mandriva.org> 1.2.0.cvs20080301-4.1mdv2011.0
+ Revision: 537991
- just a rebuild to fix the "inconsistent assumptions over interface" problem

* Sun Jun 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0.cvs20080301-4mdv2010.0
+ Revision: 390235
- rebuild

* Sat Feb 21 2009 Florent Monnier <blue_prawn@mandriva.org> 1.2.0.cvs20080301-3mdv2009.1
+ Revision: 343706
- incremented rel number
- added version in the META file

* Tue Feb 03 2009 Florent Monnier <blue_prawn@mandriva.org> 1.2.0.cvs20080301-2mdv2009.1
+ Revision: 337135
- The initial RPM release was made from the fedora rpm .spec file (revision 1.7) by Richard W.M. Jones
- import ocaml-cairo


* Tue Dec 16 2008 Florent Monnier <fmonnier@linux-nantes.org> 1.2.0.cvs20080301-1mdv
- Initial RPM release made from the redhat rpm .spec file (revision 1.7) by Richard W.M. Jones
