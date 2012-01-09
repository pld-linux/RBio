Summary:	RBio: read/write matrices in Rutherford/Boeing format
Summary(pl.UTF-8):	RBio: odczyt/zapis macierzy zapisanych w formacie Rutherforda-Boeinga
Name:		RBio
Version:	2.0.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.cise.ufl.edu/research/sparse/RBio/%{name}-%{version}.tar.gz
# Source0-md5:	fd469b4ccac07c771c10c3046d593791
Patch0:		%{name}-ufconfig.patch
Patch1:		%{name}-shared.patch
URL:		http://www.cise.ufl.edu/research/sparse/RBio/
BuildRequires:	UFconfig-devel >= 3.7.0
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RBio - MATLAB toolbox for reading/writing sparse matrices in the
Rutherford/Boeing format, and for reading/writing problems in the UF
Sparse Matrix Collection from/to a set of files in a directory.
Version 2.0 is written in C. Older versions were in Fortran.

%description -l pl.UTF-8
RBio to narzędzia MATLAB-a do odczytu/zapisu macierzy rzadkich w
formacie Rutherforda-Boeinga oraz odczytu/zapisu problemów dla
oprogramowania UF Sparse Matrix Collection z/do zbioru plików w
katalogu. Wersja 2.0 została napisana w C; wcześniejsze wersje były w
Fortranie.

%package devel
Summary:	Header files for RBio library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki RBio
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	UFconfig-devel >= 3.7.0

%description devel
Header files for RBio library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki RBio.

%package static
Summary:	Static RBio library
Summary(pl.UTF-8):	Statyczna biblioteka RBio
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static RBio library.

%description static -l pl.UTF-8
Statyczna biblioteka RBio.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/rbio

%{__make} -C Lib install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

install Include/*.h $RPM_BUILD_ROOT%{_includedir}/rbio

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt Doc/{ChangeLog,License.txt}
%attr(755,root,root) %{_libdir}/librbio.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librbio.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librbio.so
%{_libdir}/librbio.la
%{_includedir}/rbio

%files static
%defattr(644,root,root,755)
%{_libdir}/librbio.a
