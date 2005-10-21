Summary:	XSL formatter
Summary(pl):	Program formatuj±cy XSL
Name:		xmlroff
Version:	0.3.6
Release:	1
License:	distributable
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/xmlroff/%{name}-%{version}.tar.gz
# Source0-md5:	f0ced928fb248f068d99aa6a0dba4947
Patch0:		%{name}-no_static.patch
URL:		http://xmlroff.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pangopdf-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xmlroff is an XSL formatter. That is, it creates formatted output -
pages containing text in a variety of type styles and sizes - from an
input XML document and an XSL stylesheet. This processing model is
defined in the XSL Recommendation that was developed by the W3C.

%description -l pl
xmlroff to program formatuj±cy XSL - tzn. tworz±cy na wyj¶ciu
strony sformatowane zawieraj±ce tekst w ró¿nych stylach i rozmiarach
na podstawie wej¶ciowego dokumentu XML i arkusza stylu XSL. Ten model
przetwarzania zosta³ zdefiniowany w dokumencie XSL Recommendation
stworzonym przez W3C.


%package libfo
Summary:	libfo library
Summary(pl):	biblioteka libfo
Group:		Applications/Publishing/XML

%description libfo
libfo

%description libfo -l pl
libfo

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--enable-gp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README COPYING
%attr(755,root,root) %{_bindir}/*
%{_gtkdocdir}/xmlroff

%files libfo
%{_datadir}/xml/libfo-%{version}
%attr(755,root,root) %{_libdir}/libfo-*.so.*
%{_pkgconfigdir}/libfo-0.3.pc
