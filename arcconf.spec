%define		fver	7_31
%define		ver		%(echo %{fver} | tr _ .)
%define		subver	18856
Summary:	Adaptec uniform command line interface
Summary(pl.UTF-8):	Ujednolicony interfejs linii poleceń Adapteca
Name:		arcconf
Version:	%{ver}.%{subver}
Release:	1
License:	Adaptec Downloadable Software License
Group:		Base
# tgz tarballs originaly came from 30MB+ Storage Manager RPM Files
Source0:	http://download.adaptec.com/raid/storage_manager/asm_linux_x86_v%{fver}_%{subver}.tgz
# Source0-md5:	2bdfd5e999a86ac5bd8c7b43d858fdfd
Source1:	http://download.adaptec.com/raid/storage_manager/asm_linux_x64_v%{fver}_%{subver}.tgz
# Source1-md5:	f9f13c1f9223da6138abc2c8bdadd54a
URL:		http://www.adaptec.com/en-us/downloads/storage_manager/sm/productid=sas-5805zq&dn=adaptec+raid+5805zq.html
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin
%define		_enable_debug_packages	0

%description
Adaptec Storage Manager Command Line Utility.

Compatible Products:
- Adaptec RAID 2045
- Adaptec RAID 2405
- Adaptec RAID 2405Q
- Adaptec RAID 2805
- Adaptec RAID 5085
- Adaptec RAID 5405
- Adaptec RAID 5405Z
- Adaptec RAID 5445
- Adaptec RAID 5445Z
- Adaptec RAID 5805
- Adaptec RAID 5805Q
- Adaptec RAID 5805Z
- Adaptec RAID 5805ZQ
- Adaptec RAID 51245
- Adaptec RAID 51645
- Adaptec RAID 52445
- Adaptec RAID 6405
- Adaptec RAID 6405E
- Adaptec RAID 6405T
- Adaptec RAID 6445
- Adaptec RAID 6805
- Adaptec RAID 6805E
- Adaptec RAID 6805T
- Adaptec RAID 6805TQ
- Adaptec RAID 6805Q

%description -l pl.UTF-8
Obsługiwane z linii poleceń narzędzie do zarządzania kontrolerami
Adapteca.

Obsługiwane kontrolery:
- Adaptec RAID 2045
- Adaptec RAID 2405
- Adaptec RAID 2405Q
- Adaptec RAID 2805
- Adaptec RAID 5085
- Adaptec RAID 5405
- Adaptec RAID 5405Z
- Adaptec RAID 5445
- Adaptec RAID 5445Z
- Adaptec RAID 5805
- Adaptec RAID 5805Q
- Adaptec RAID 5805Z
- Adaptec RAID 5805ZQ
- Adaptec RAID 51245
- Adaptec RAID 51645
- Adaptec RAID 52445
- Adaptec RAID 6405
- Adaptec RAID 6405E
- Adaptec RAID 6405T
- Adaptec RAID 6445
- Adaptec RAID 6805
- Adaptec RAID 6805E
- Adaptec RAID 6805T
- Adaptec RAID 6805TQ
- Adaptec RAID 6805Q

%prep
%ifarch %{ix86}
%setup -qTc -a0
%endif
%ifarch %{x8664}
%setup -qTc -a1
%endif
mv cmdline/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -p arcconf $RPM_BUILD_ROOT%{_sbindir}/arcconf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc README.TXT
%attr(755,root,root) %{_sbindir}/arcconf
