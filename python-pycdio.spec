#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

Summary:	Python 2 bindings for libcdio
Summary(pl.UTF-8):	Wiązania Pythona 2 do libcdio
Name:		python-pycdio
Version:	2.1.0
Release:	4
License:	GPL v2+
Group:		Libraries/Python
Source0:	https://ftp.gnu.org/gnu/libcdio/pycdio-%{version}.tar.gz
# Source0-md5:	d1adcee07dc0f510a983547bf5046632
URL:		http://www.gnu.org/software/libcdio/
BuildRequires:	libcdio-devel >= 2.0.0
BuildRequires:	pkgconfig
%if %{with python2}
BuildRequires:	python-devel >= 1:2.3.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	swig-python >= 3
Requires:	libcdio >= 2.0.0
Requires:	python-libs >= 1:2.3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 bindings for libcdio.

%description -l pl.UTF-8
Wiązania Pythona 2 do libcdio.

%package -n python3-pycdio
Summary:	Python 3 bindings for libcdio
Summary(pl.UTF-8):	Wiązania Pythona 3 do libcdio
Group:		Libraries/Python
Requires:	libcdio >= 2.0.0
Requires:	python3-libs >= 1:3.2

%description -n python3-pycdio
Python 3 bindings for libcdio.

%description -n python3-pycdio -l pl.UTF-8
Wiązania Pythona 3 do libcdio.

%package examples
Summary:	Example programs using Python libcdio bindings
Summary(pl.UTF-8):	Przykładowe programy w Pythonie używające libcdio
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Example programs using Python libcdio bindings.

%description examples -l pl.UTF-8
Przykładowe programy w Pythonie używające libcdio.

%prep
%setup -q -n pycdio-%{version}

%{__sed} -i -e '1s,#!.*python,#!%{__python3},' example/*.py

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install example/{*.py,README} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc ChangeLog README.rst THANKS
%attr(755,root,root) %{py_sitedir}/_pycdio.so
%attr(755,root,root) %{py_sitedir}/_pyiso9660.so
%{py_sitedir}/cdio.py[co]
%{py_sitedir}/iso9660.py[co]
%{py_sitedir}/pycdio.py[co]
%{py_sitedir}/pyiso9660.py[co]
%{py_sitedir}/pycdio-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pycdio
%defattr(644,root,root,755)
%doc ChangeLog README.rst THANKS
%attr(755,root,root) %{py3_sitedir}/_pycdio.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/_pyiso9660.cpython-*.so
%{py3_sitedir}/cdio.py
%{py3_sitedir}/iso9660.py
%{py3_sitedir}/pycdio.py
%{py3_sitedir}/pyiso9660.py
%{py3_sitedir}/__pycache__/cdio.cpython-*.py[co]
%{py3_sitedir}/__pycache__/iso9660.cpython-*.py[co]
%{py3_sitedir}/__pycache__/pycdio.cpython-*.py[co]
%{py3_sitedir}/__pycache__/pyiso9660.cpython-*.py[co]
%{py3_sitedir}/pycdio-%{version}-py*.egg-info
%endif

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
