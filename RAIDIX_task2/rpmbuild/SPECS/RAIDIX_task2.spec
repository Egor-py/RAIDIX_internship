Name:           RAIDIX_task2
Version:        1.0.1
Release:        1%{?dist}
Summary:        TestTask2

License:        X11 License
URL:            https://github.com/Egor-py/RAIDIX_internship/tree/main/RAIDIX_task1
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  python3
Requires:       python3 hiredis = 3.6.8

%description


%prep
%{__rm} -rf %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
%{__tar} -xzvf %{SOURCE0} -C %{_builddir}/%{name}-%{version} --strip-components 1


%build
cd %{name}-%{version}
%{__make}

%install
cd %{name}-%{version}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf $RPM_BUILDROOT
%{__rm} -rf $RPM_BUILD_DIR/*

%files
%defattr(-,root,root)

%changelog
* Sat Oct 29 2022 builder
-
