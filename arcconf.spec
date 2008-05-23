Summary:	Adaptec uniform command line interface
Name:		arcconf
Version:	5.30
Release:	1
License:	Unknown
Group:		Base
Source0:	http://www.obvious.co.nz/aacraid/arcconf/%{name}-5.3-b17509.tgz
# Source0-md5:	d1b46891dcf0c6a9a4cde9e3c82bb594
# From adaptec CD, ver 5.20
Source1:	%{name}64
# Source1-md5:	140dfcade7c191d72970558a0177060a
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
