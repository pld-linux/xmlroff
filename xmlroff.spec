Summary:	XSL formatter
Summary(pl):	Program formatuj�cy XSL
Name:		xmlroff
Version:	0.2.2
Release:	0.1
License:	distributable
Group:		Applications/Publishing/XML
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://xmlroff.sourceforge.net/
BuildRequires:	pangopdf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xmlroff is an XSL formatter. That is, it creates formatted output -
pages containing text in a variety of type styles and sizes - from an
input XML document and an XSL stylesheet. This processing model is
defined in the XSL Recommendation that was developed by the W3C.

%description -l pl
xmlroff to program formatuj�cy XSL - tzn. tworz�cy na wyj�ciu
strony sformatowane zawieraj�ce tekst w r�nych stylach i rozmiarach
na podstawie wej�ciowego dokumentu XML i arkusza stylu XSL. Ten model
przetwarzania zosta� zdefiniowany w dokumencie XSL Recommendation
stworzonym przez W3C.

%prep
%setup -q

%build
%configure
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
%{_datadir}/%{name}
