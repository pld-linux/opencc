#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Open Chinese Convert library
Summary(pl.UTF-8):	Biblioteka Open Chinese Convert do konwersji między wariantami języka chińskiego
Name:		opencc
Version:	1.0.6
Release:	3
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://github.com/BYVoid/OpenCC/releases
Source0:	https://github.com/BYVoid/OpenCC/archive/ver.%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bcb6d42f6f0eedabaf95c71627f725a9
Patch0:		%{name}-paths.patch
URL:		https://github.com/BYVoid/OpenCC
BuildRequires:	cmake >= 2.8
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	rpmbuild(macros) >= 1.605
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
Requires:	libstdc++-devel >= 6:4.7

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
%setup -q -n OpenCC-ver.%{version}
%patch0 -p1

%build
%if %{with static_libs}
install -d build-static
cd build-static
%cmake .. \
	-DBUILD_SHARED_LIBS=OFF

%{__make} -j1
cd ..
%endif

install -d build
cd build
%cmake ..

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%if %{with static_libs}
%{__make} -C build-static install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS.md README.md
%attr(755,root,root) %{_bindir}/opencc
%attr(755,root,root) %{_bindir}/opencc_dict
%attr(755,root,root) %{_bindir}/opencc_phrase_extract
%attr(755,root,root) %{_libdir}/libopencc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopencc.so.2
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopencc.so
%{_includedir}/opencc
%{_pkgconfigdir}/opencc.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libopencc.a
%endif
