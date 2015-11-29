%define 	module	autopy
Summary:	A simple, cross-platform GUI automation toolkit for Python.
Summary(pl.UTF-8):	Proste wieloplatforme narzędzie automaytzacji GUI dla Pythona.
Name:		python-%{module}
Version:	0.51
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/a/autopy/autopy-0.51.tar.gz
# Source0-md5:	b92055aa2a3712a9c3b4c874014b450e
URL:		http://www.autopy.org/
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:		python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AutoPy is a simple, cross-platform GUI automation toolkit for Python. It includes functions for controlling the keyboard and mouse, finding colors and bitmaps on-screen, and displaying alerts -- 
all in a cross-platform, efficient, and simple manner.

%description -l pl.UTF-8
AutoPy to proste wieloplatforme narzędzie automaytzacji GUI dla Pythona.
Zawiera funkcje do kontorli klawiatury i myszki, wynajdywania kolorów i bitma na ekranie, oraz wyświetlania dialogów ostrzeżeń.
Wszystko w międzyplaformowy, efektywny i prosty sposób.

%prep
%setup -q -n %{module}-%{version}


%build
%py_build


%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}-%{version}-*.egg-info
%endif

