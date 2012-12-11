%define fname	PythonDaap

Name:		python-daap
Summary:	DAAP client written in Python
Version:	0.7.1
Release:	%{mkrel 3}
Source0:	http://jerakeen.org/files/%{fname}-%{version}.tar.gz
URL:		http://jerakeen.org/code/pythondaap/
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	LGPL+
BuildRequires:	python
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	intltool
Requires:	python

%description
PythonDaap is a (under development) DAAP client implemented in Python,
and based on PyTunes by Davyd Madeley.

%prep
%setup -q -n %{fname}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot} --compile --optimize=2

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGELOG README PKG-INFO
%{py_platsitedir}/*



%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.7.1-3mdv2010.0
+ Revision: 442091
- rebuild

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 0.7.1-2mdv2009.1
+ Revision: 319525
- rebuild with python 2.6

* Thu Apr 17 2008 Adam Williamson <awilliamson@mandriva.org> 0.7.1-1mdv2009.0
+ Revision: 195313
- drop patch (merged upstream)
- new release 0.7.1

* Thu Mar 13 2008 Adam Williamson <awilliamson@mandriva.org> 0.7-2mdv2008.1
+ Revision: 187382
- add x86_64_crash.patch to fix the x86-64 crash reported by erwan and anne (from upstream via Debian bug #426046)

* Sun Mar 09 2008 Adam Williamson <awilliamson@mandriva.org> 0.7-1mdv2008.1
+ Revision: 182730
- import python-daap


