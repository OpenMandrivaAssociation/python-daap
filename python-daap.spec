%define fname	PythonDaap

Name:		python-daap
Summary:	DAAP client written in Python
Version:	0.7.1
Release:	%{mkrel 1}
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

