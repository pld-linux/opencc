Summary:	Open Chinese Convert library
Summary(pl.UTF-8):	Biblioteka Open Chinese Convert do konwersji między wariantami języka chińskiego
Name:		opencc
Version:	0.4.3
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: http://code.google.com/p/opencc/downloads/list
Source0:	http://opencc.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	e803b4419872c97d984d25544eef2951
URL:		http://code.google.com/p/opencc/
BuildRequires:	cmake >= 2.8
BuildRequires:	gettext-tools
BuildRequires:	rpmbuild(macros) >= 1.603
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenCC (Open Chinese Convert) is an opensource project for conversion
between Traditional Chinese and Simplified Chinese, which supports
phrase-level conversion and regional idioms among Mainland China,
Taiwan and Hong Kong.

%description -l pl.UTF-8
OpenCC (Open Chinese Convert) to projekt o otwartych źródłach, którego
celem jest konwersja między chińskim tradycyjnym a chińskim
uproszczonym, obsługujący tłumaczenie na poziomie fraz oraz idiomy
lokalne specyficzne dla Chin lądowych, Tajwanu i Hongkongu.

%package devel
Summary:	Header files for OpenCC library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenCC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for OpenCC library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenCC.

%package static
Summary:	Static OpenCC library
Summary(pl.UTF-8):	Statyczna biblioteka OpenCC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenCC library.

%description static -l pl.UTF-8
Statyczna biblioteka OpenCC.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DENABLE_GETTEXT=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS.md README.md
%attr(755,root,root) %{_bindir}/opencc
%attr(755,root,root) %{_bindir}/opencc_dict
%attr(755,root,root) %{_libdir}/libopencc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopencc.so.1
%{_datadir}/%{name}
%{_mandir}/man1/opencc.1*
%{_mandir}/man1/opencc_dict.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopencc.so
%{_includedir}/opencc
%{_pkgconfigdir}/opencc.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libopencc.a
