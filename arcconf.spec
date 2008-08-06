Summary:	Adaptec uniform command line interface
Name:		arcconf
Version:	6.0
Release:	1
License:	Adaptec Downloadable Software License
Group:		Base
Source0:	http://www.obvious.co.nz/aacraid/arcconf/%{name}-6.0-b17922.tgz 
Source1:	http://www.obvious.co.nz/aacraid/arcconf/%{name}-x64-6.0-b17922.tgz
# Source1-md5:	70684147e6e04cdbdad1891c6b8e6799
URL:		http://linux.adaptec.com/
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

%prep
%setup -q -c -a1
%ifarch %{ix86}
install linux/cmdline/{arcconf,README.TXT} .
%endif
%ifarch %{x8664}
install linux-x64/cmdline/{arcconf,README.TXT} .
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
%doc README.TXT
%attr(755,root,root) %{_sbindir}/*
