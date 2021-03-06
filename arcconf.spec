%define		fver	2_05
%define		ver		%(echo %{fver} | tr _ .)
%define		subver	22932
Summary:	Adaptec uniform command line interface
Summary(pl.UTF-8):	Ujednolicony interfejs linii poleceń Adapteca
Name:		arcconf
Version:	%{ver}.%{subver}
Release:	2
Epoch:		1
License:	Adaptec Downloadable Software License
Group:		Base
# link from any lastest adaptec controller download
Source0:	http://download.adaptec.com/raid/storage_manager/%{name}_v%{fver}_%{subver}.zip
# Source0-md5:	51a03b5fe08b45f229b2c73127c5c6ae
URL:		http://storage.microsemi.com/en-us/downloads/storage_manager/sm/productid=asr-81605zq&dn=adaptec+raid+81605zq.php
ExclusiveArch:	%{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin
%define		_enable_debug_packages	0

%description
Adaptec Storage Manager Command Line Utility.

Compatible Products:
- Adaptec RAID 6405
- Adaptec RAID 6405E
- Adaptec RAID 6405T
- Adaptec RAID 6445
- Adaptec RAID 6805
- Adaptec RAID 6805E
- Adaptec RAID 6805T
- Adaptec RAID 6805TQ
- Adaptec RAID 6805Q
- Adaptec RAID 7805
- Adaptec RAID 7805Q
- Adaptec RAID 78165
- Adaptec RAID 71605E
- Adaptec RAID 71605
- Adaptec RAID 71605Q
- Adaptec RAID 71685
- Adaptec RAID 72405
- Adaptec RAID 8805
- Adaptec RAID 8885
- Adaptec RAID 8885Q
- Adaptec RAID 81605ZQ

%description -l pl.UTF-8
Obsługiwane z linii poleceń narzędzie do zarządzania kontrolerami
Adapteca.

Obsługiwane kontrolery:
- Adaptec RAID 6405
- Adaptec RAID 6405E
- Adaptec RAID 6405T
- Adaptec RAID 6445
- Adaptec RAID 6805
- Adaptec RAID 6805E
- Adaptec RAID 6805T
- Adaptec RAID 6805TQ
- Adaptec RAID 6805Q
- Adaptec RAID 7805
- Adaptec RAID 7805Q
- Adaptec RAID 78165
- Adaptec RAID 71605E
- Adaptec RAID 71605
- Adaptec RAID 71605Q
- Adaptec RAID 71685
- Adaptec RAID 72405
- Adaptec RAID 8805
- Adaptec RAID 8885
- Adaptec RAID 8885Q
- Adaptec RAID 81605ZQ

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install -p linux_x64/cmdline/arcconf $RPM_BUILD_ROOT%{_sbindir}/arcconf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/arcconf
