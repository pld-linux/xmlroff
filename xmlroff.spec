
#
# TODO : libfo subpackage, but I dont think any other package may use it.
#        build with enable-gp - currently there is a problem with linking against pango-1.0.so from xmlroof.
#

Summary:	XSL formatter
Summary(pl):	Program formatuj±cy XSL
Name:		xmlroff
Version:	0.2.8
Release:	3
License:	distributable
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/xmlroff/%{name}-%{version}.tar.gz
# Source0-md5:	810e545c44cb9716983bee6a89458be6
Patch0:		%{name}-no_static.patch
URL:		http://xmlroff.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pangopdf-devel
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
	--enable-pdflib \
	--disable-gp
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
%attr(755,root,root) %{_libdir}/libfo-*.so.*
%{_gtkdocdir}/xmlroff
