%define	name	t38modem
%define	version	0.8.0
%define	snap	20050322
%define	release	%mkrel 0.%{snap}.4

%{expand:%%define o_ver %(echo v%{version}| sed "s#\.#_#g")}
%define openh323_version 1.15.3
%define pwlib_version 1.8.4

Summary:	H.323 fax (T.38) client
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MPL
Group:		Communications
URL:		http://openh323.sourceforge.net/
Source0:	%{name}-%{o_ver}-%{snap}-src.tar.bz2
Patch0:		t38modem-mak_files.diff
BuildRequires:	openh323-devel >= %{openh323_version} pwlib-devel >= %{pwlib_version}
Conflicts:	vpb-devel
Requires:	openh323_1 >= %{openh323_version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a H.323 fax (T.38) client, T38FAX Pseudo Modem.

 o From your fax application view point it's a fax modem pool.
 o From IP network view point it's a H.323 endpoint with T.38 fax
   support.
 o From your view point it's a gateway between a fax application
   and IP network.

%prep

%setup -q -n %{name}
%patch0 -p0

chmod 644 CHANGES README HylaFAX/config.ttyx

%build

export CFLAGS="%{optflags} -DLDAP_DEPRECATED"
export CXXFLAGS="%{optflags} -DLDAP_DEPRECATED"

%make \
    OPTCCFLAGS="%{optflags}" \
    PWLIBDIR=%{_datadir}/pwlib \
    OPENH323DIR=%{_prefix} \
    PREFIX=%{_prefix} \
    PWLIB_BUILD=1 \
    optshared \

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 obj_*/%{name} %{buildroot}%{_bindir}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc CHANGES README HylaFAX/config.ttyx
%attr(0755,root,root) %{_bindir}/*

