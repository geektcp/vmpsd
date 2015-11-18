Name: vmpsd
Summary: VLAN Management Policy Server daemon
Epoch: 1
Version: 1.3
Release: 1a
Copyright: distributable
Group: System Environment/Daemons
Source0: vmpsd-%{version}.tar.gz
Source1: vmpsd.init
Source2: vmpsd.conf
Source3: vmpsd.sysinit
Source4: vmpsd.readme
URL: http://vmps.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prereq: /sbin/chkconfig
Requires: kernel >= 2.2.18

%description

OpenVMPS is a GPL implementation of Cisco's VLAN Management Policy
Server as used on the Catalyst 5500 family of switches.  It is used on
Cisco LAN switces to dynamically assign ports to VLANs according to
Ethernet Address.  Because it was developed solely on infomation
obtained by observing the network traffic between switches it is
probably not complete but it is a working subset of the protocol.  You
can find more information on VMPS at www.cisco.com.

%prep
%setup -q
#./configure --prefix=/usr --sysconfdir=/etc
%configure

%build
make

%install

rm -rf %{buildroot}
cp %SOURCE4 .

mkdir -p %{buildroot}/etc/rc.d/init.d
mkdir -p %{buildroot}/etc/sysconfig
mkdir -p %{buildroot}/usr/sbin

install -m 0755 vmpsd %{buildroot}/usr/sbin/vmpsd
install -m 0755 %SOURCE1 %{buildroot}/etc/rc.d/init.d/vmpsd
install -m 0755 %SOURCE2 %{buildroot}/etc/vmpsd.conf
install -m 0755 %SOURCE3 %{buildroot}/etc/sysconfig/vmpsd

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add vmpsd

%files
%defattr(-,root,root)
%config(noreplace) /etc/vmpsd.conf
/etc/rc.d/init.d/vmpsd
/etc/sysconfig/vmpsd
%{_sbindir}/vmpsd
%doc README NEWS vmpsd.readme doc/vlan.db.example doc/VQP-spec.txt

%changelog
* Wed May 26 2004 Jay Leafey <jleafey@utmem.edu> 1:1.1-1a
- Cleaned up the specfile, added more documentation

* Mon Apr 12 2004 Jay Leafey <jleafey@utmem.edu> 1:1.1-1
- First package.
