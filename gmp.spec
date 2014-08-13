Summary:	GNU arbitrary precision library
Name:		gmp
Version:	6.0.0
Release:	2
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnu.org/gnu/gmp/%{name}-%{version}a.tar.xz
# Source0-md5:	1e6da4e434553d2811437aa42c7f7c76
URL:		http://www.swox.com/gmp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gmp package contains GNU MP, a library for arbitrary precision
arithmetic, signed integers operations, rational numbers and floating
point numbers. GNU MP is designed for speed, for both small and very
large operands. GNU MP is fast for several reasons: It uses fullwords
as the basic arithmetic type, it uses fast algorithms, it carefully
optimizes assembly code for many CPUs' most common inner loops and it
generally emphasizes speed over simplicity/elegance in its operations.

Install the gmp package if you need a fast arbitrary precision
library.

%package devel
Summary:	GNU Arbitrary Precision header files, static libraries, and documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The static libraries, header files and documentation for using the GNU
MP arbitrary precision library in applications.

If you want to develop applications which will use the GNU MP library,

%package c++
Summary:	GNU arbitrary precision library - C++ interface
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description c++
C++ class interface to GNU arbitrary precision library.

%package c++-devel
Summary:	GNU arbitrary precition library - C++ interface headers
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description c++-devel
Header files for C++ class interface to GNU arbitrary precision
library.

%prep
%setup -q

%build
mkdir build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd build
../%configure \
	--disable-static	\
	--enable-cxx		\
	--enable-fft
%{__make}
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%post	c++ -p /usr/sbin/ldconfig
%postun	c++ -p /usr/sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libgmp.so.??
%attr(755,root,root) %{_libdir}/libgmp.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmp.so
%{_libdir}/libgmp.la
%{_includedir}/gmp.h
%{_infodir}/gmp.info*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgmpxx.so.?
%attr(755,root,root) %{_libdir}/libgmpxx.so.*.*.*

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgmpxx.so
%{_libdir}/libgmpxx.la
%{_includedir}/gmpxx.h

