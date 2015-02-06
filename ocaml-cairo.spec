%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	OCaml library for accessing cairo graphics
Name:		ocaml-cairo
Version:	1.2.0.1
Release:	7
License:	LGPLv2+
Group:		Development/Other
Url:		http://cairographics.org/cairo-ocaml/
Source0:	ocaml-cairo-%{version}.tar.gz
Source1:	ocaml-cairo-META
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-lablgtk2
BuildRequires:	ocaml-lablgtk2-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libsvg-cairo)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	chrpath
Requires:	ocaml-lablgtk2

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

%files
%doc COPYING
%{_libdir}/ocaml/cairo
%exclude %{_libdir}/ocaml/cairo/*.a
%exclude %{_libdir}/ocaml/cairo/*.cmxa
%exclude %{_libdir}/ocaml/cairo/*.cmx
%exclude %{_libdir}/ocaml/cairo/*.mli
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}
Requires:	ocaml-lablgtk2-devel
Requires:	pkgconfig(cairo)

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc COPYING ChangeLog README doc/html
%{_libdir}/ocaml/cairo/*.a
%{_libdir}/ocaml/cairo/*.cmxa
%{_libdir}/ocaml/cairo/*.cmx
%{_libdir}/ocaml/cairo/*.mli

#----------------------------------------------------------------------------

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
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
ocamlfind install cairo src/{*.mli,*.cmi,*.cma,*.a,*.cmxa,*.cmx,dll*.so} META

strip %{buildroot}%{_libdir}/ocaml/stublibs/dll*.so
chrpath --delete %{buildroot}%{_libdir}/ocaml/stublibs/dll*.so

