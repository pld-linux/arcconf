Summary:	Adaptec uniform command line interface
Name:		arcconf
Version:	6.0
Release:	1
License:	Adaptec Downloadable Software License
Group:		Base
Source0:	http://www.obvious.co.nz/aacraid/arcconf/%{name}-6.0-b17922.tgz 
# Source0-md5:	222c459447edbe7e836324056408bb0b
# From http://download.adaptec.com/raid/storage_manager/asm_linux_x64_v5_30_17509.rpm
# v5.30
Source1:	%{name}64
# Source1-md5:	c1add88f7c7f8a8a333ac9c823ad42d3
URL:		http://linux.adaptec.com/
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin

%description
Adaptec Storage Manager Command Line Utility.

Compatible Products:
- Adaptec RAID 3085
- Adaptec RAID 31205
- Adaptec RAID 31605
- Adaptec RAID 3405
- Adaptec RAID 3805

%prep
%setup -q -c
%ifarch %{ix86}
install linux/cmdline/arcconf .
%endif
%ifarch %{x8664}
install %{SOURCE1} arcconf
%endif

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install arcconf $RPM_BUILD_ROOT%{_sbindir}/arcconf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
