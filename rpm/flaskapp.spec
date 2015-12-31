%define name flaskapp
%define version $VERSION

%if 0%{?rhel} == 5
%define __python /usr/bin/python26
%endif

Name:      %{name}
Version:   %{version}
Release:   1%{?dist}
Url:       http://www.ansible.com
Summary:   Tiny Flask app
License:   GPLv3
Group:     Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
BuildArch: noarch
Requires: python

%description
This really doesn't do very much

%prep
%{__make} test

%build

%install

mkdir -p %{buildroot}/etc/ansible/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/ansible*
%{_bindir}/ansible*
%dir %{_datadir}/ansible
%config(noreplace) %{_sysconfdir}/ansible
%doc README.md PKG-INFO COPYING
%doc %{_mandir}/man1/ansible*

%changelog

* Sat Dec 12 2015 Mark Phillips <mark@ansible.com> - 1.0.0
- Initial release
