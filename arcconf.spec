%define		ver	6.50
%define		build	18771
Summary:	Adaptec uniform command line interface
Summary(pl.UTF-8):	Ujednolicony interfejs linii poleceń Adapteca
Name:		arcconf
Version:	%{ver}.%{build}
Release:	1
License:	Adaptec Downloadable Software License
Group:		Base
# tgz tarballs originaly came from 30MB+ Storage Manager RPM Files
Source0:	http://www.obvious.co.nz/aacraid/arcconf/%{name}-%{ver}-b%{build}.tgz
# Source0-md5:	8c3ccd6e2098293e5653ce69451f4d12
Source1:	http://www.obvious.co.nz/aacraid/arcconf/%{name}-x64-%{ver}-b%{build}.tgz
# Source1-md5:	a5b4b313ec86023b035f5c3105c01049
Source2:	http://www.obvious.co.nz/aacraid/arcconf/CLI_v6_50_%{build}_Users_Guide.pdf
# Source2-md5:	273d2e2d867c9fe94f12b363ba816094
URL:		http://www.adaptec.com/en-US/downloads/storage_manager/sm?productId=SAS-3405
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin
%define		_enable_debug_packages	0

%description
Adaptec Storage Manager Command Line Utility.

Compatible Products:
- Adaptec RAID 3085
- Adaptec RAID 31205
- Adaptec RAID 31605
- Adaptec RAID 3405
- Adaptec RAID 3805

%description -l pl.UTF-8
Obsługiwane z linii poleceń narzędzie do zarządzania kontrolerami
Adapteca.

Obsługiwane kontrolery:
- Adaptec RAID 3085
- Adaptec RAID 31205
- Adaptec RAID 31605
- Adaptec RAID 3405
- Adaptec RAID 3805

%prep
%ifarch %{ix86}
%setup -qTc -a0
%endif
%ifarch %{x8664}
%setup -qTc -a1
%endif
mv linux*/cmdline/* .

install %{SOURCE2} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -p arcconf $RPM_BUILD_ROOT%{_sbindir}/arcconf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.TXT *.pdf
%attr(755,root,root) %{_sbindir}/*
