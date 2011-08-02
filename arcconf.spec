%define		ver	7.0
%define		build	18781
Summary:	Adaptec uniform command line interface
Summary(pl.UTF-8):	Ujednolicony interfejs linii poleceń Adapteca
Name:		arcconf
Version:	%{ver}.%{build}
Release:	1
License:	Adaptec Downloadable Software License
Group:		Base
# tgz tarballs originaly came from 30MB+ Storage Manager RPM Files
Source0:	http://www.obvious.co.nz/aacraid/arcconf/%{name}-%{ver}-b%{build}.tgz
# Source0-md5:	19c0c942a5acb0024a2edb844e3bdbcf
Source1:	http://www.obvious.co.nz/aacraid/arcconf/%{name}-x64-%{ver}-b%{build}.tgz
# Source1-md5:	ad37a2c0c3e38060b96069651421255d
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -p arcconf $RPM_BUILD_ROOT%{_sbindir}/arcconf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.TXT
%attr(755,root,root) %{_sbindir}/*
