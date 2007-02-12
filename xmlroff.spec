#
# Conditional build:
%bcond_without	gnomeprint	# disable GNOME Print backend
#
Summary:	XSL formatter
Summary(pl.UTF-8):   Program formatujący XSL
Name:		xmlroff
Version:	0.3.6
Release:	1
License:	BSD-like
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/xmlroff/%{name}-%{version}.tar.gz
# Source0-md5:	f0ced928fb248f068d99aa6a0dba4947
Patch0:		%{name}-no_static.patch
Patch1:		%{name}-link.patch
URL:		http://xmlroff.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	gtk-doc >= 0.10
BuildRequires:	gtk+2-devel >= 1:2.2.0
%{?with_gnomeprint:BuildRequires:	libgnomeprint-devel >= 2.8}
BuildRequires:	libtool
BuildRequires:	pangoxsl-devel >= 1.6
BuildRequires:	libxml2-devel >= 2.4.3
BuildRequires:	libxslt-devel >= 1.0.3
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 0.5
BuildRequires:	popt-devel
Requires:	%{name}-libfo = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xmlroff is an XSL formatter. That is, it creates formatted output -
pages containing text in a variety of type styles and sizes - from an
input XML document and an XSL stylesheet. This processing model is
defined in the XSL Recommendation that was developed by the W3C.

%description -l pl.UTF-8
xmlroff to program formatujący XSL - tzn. tworzący na wyjściu
strony sformatowane zawierające tekst w różnych stylach i rozmiarach
na podstawie wejściowego dokumentu XML i arkusza stylu XSL. Ten model
przetwarzania został zdefiniowany w dokumencie XSL Recommendation
stworzonym przez W3C.

%package libfo
Summary:	libfo - XSL formatter library
Summary(pl.UTF-8):   libfo - biblioteka formatowania XSL
Group:		Libraries
Requires:	glib2 >= 1:2.4.0
Requires:	gtk+2 >= 1:2.2.0
%{?with_gnomeprint:Requires:	libgnomeprint >= 2.8}
Requires:	pangoxsl >= 1.6
Requires:	libxml2 >= 2.4.3

%description libfo
libfo - XSL formatter library.

%description libfo -l pl.UTF-8
libfo - biblioteka formatowania XSL.

%package libfo-devel
Summary:	Header files for libfo library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libfo
Group:		Development/Libraries
Requires:	%{name}-libfo = %{version}-%{release}
Requires:	glib2-devel >= 1:2.4.0
Requires:	gtk+2-devel >= 1:2.2.0
%{?with_gnomeprint:Requires:	libgnomeprint-devel >= 2.8}
Requires:	pangoxsl-devel >= 1.6
Requires:	libxml2-devel >= 2.4.3

%description libfo-devel
Header files for libfo library.

%description libfo-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libfo.

%package libfo-static
Summary:	Static libfo library
Summary(pl.UTF-8):   Statyczna biblioteka libfo
Group:		Development/Libraries
Requires:	%{name}-libfo-devel = %{version}-%{release}

%description libfo-static
Static libfo library.

%description libfo-static -l pl.UTF-8
Statyczna biblioteka libfo.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_gnomeprint:--disable-gp} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libfo -p /sbin/ldconfig
%postun	libfo -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_gtkdocdir}/xmlroff

%files libfo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfo-*.so.*.*.*
%{_datadir}/xml/libfo-%{version}

%files libfo-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfo-*.so
%{_libdir}/libfo-*.la
%{_includedir}/libfo-*
%{_pkgconfigdir}/libfo-0.3.pc

%files libfo-static
%defattr(644,root,root,755)
%{_libdir}/libfo-*.a
