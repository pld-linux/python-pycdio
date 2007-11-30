Summary:	Python bindings for libcdio
Summary(pl.UTF-8):	Wiązania Pythona do libcdio
Name:		python-pycdio
Version:	0.13
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://ftp.gnu.org/gnu/libcdio/pycdio-%{version}.tar.gz
# Source0-md5:	dc54be352c00457e8c040cd19a434cf0
URL:		http://www.gnu.org/software/libcdio/
BuildRequires:	libcdio-devel >= 0.76
BuildRequires:	python >= 1:2.3.5
BuildRequires:	rpm-pythonprov
BuildRequires:	swig-python
%pyrequires_eq	python-libs
Requires:	libcdio >= 0.76
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for libcdio.

%description -l pl.UTF-8
Wiązania Pythona do libcdio.

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

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install example/{*.py,README} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm $RPM_BUILD_ROOT%{py_sitedir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog* NEWS README
%attr(755,root,root) %{py_sitedir}/_pycdio.so
%attr(755,root,root) %{py_sitedir}/_pyiso9660.so
%{py_sitedir}/cdio.py[co]
%{py_sitedir}/iso9660.py[co]
%{py_sitedir}/pycdio.py[co]
%{py_sitedir}/pyiso9660.py[co]

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
