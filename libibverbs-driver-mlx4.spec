Summary:	Userspace driver for the Mellanox ConnectX InfiniBand HCAs
Summary(pl.UTF-8):	Sterownik przestrzeni użytkownika dla kart Mellanox ConnectX InfiniBand HCA
Name:		libibverbs-driver-mlx4
Version:	1.2.1
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	https://www.openfabrics.org/downloads/mlx4/libmlx4-%{version}.tar.gz
# Source0-md5:	c09b34b427fa4bccae38a10c9758fc34
URL:		http://openib.org/
BuildRequires:	libibverbs-devel >= 1.1.8
Requires:	libibverbs >= 1.1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libmlx4 is a userspace driver for Mellanox ConnectX InfiniBand HCAs.
It works as a plug-in module for libibverbs that allows programs to
use Mellanox hardware directly from userspace.

Currently the driver supports HCAs on PCI Express interface based on
MT25408 ConnectX chip, using mlx4_ib kernel driver.

%description -l pl.UTF-8
libmlx4 to sterownik przestrzeni użytkownika dla kart Mellanox
ConnectX InfiniBand HCA. Działa jako moduł ładowany przez libibverbs,
pozwalający programom na dostęp z przestrzeni użytkownika do sprzętu
Mellanox.

Obecnie sterownik obsługuje kontrolery HCA na szynie PCI Express
oparte na układzie MT25408 ConnectX poprzez sterownik jądra mlx4_ib.

%package static
Summary:	Static version of mlx4 driver
Summary(pl.UTF-8):	Statyczna wersja sterownika mlx4
Group:		Development/Libraries
Requires:	libibverbs-static >= 1.1.8

%description static
Static version of mlx4 driver, which may be linked directly into
application.

%description static -l pl.UTF-8
Statyczna wersja sterownika mlx4, którą można wbudować bezpośrednio
w aplikację.

%prep
%setup -q -n libmlx4-%{version}

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened by -rdmav2.so name
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmlx4.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/libmlx4-rdmav2.so
%{_sysconfdir}/libibverbs.d/mlx4.driver

%files static
%defattr(644,root,root,755)
%{_libdir}/libmlx4.a
