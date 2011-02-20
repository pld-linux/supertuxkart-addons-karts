
Summary:	Additional karts for SuperTuxKart
Summary(pl.UTF-8):	Dodatkowe karty dla SuperTuxKart
Name:		supertuxkart-addons-karts
Version:	0.7
Release:	1
License:	Distributable
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/supertuxkart/karts_addons_%{version}.zip
# Source0-md5:	141165fc0a894c1216257261d3d54a1c
URL:		http://supertuxkart.sourceforge.net/
BuildRequires:	unzip
Requires:	supertuxkart >= 0.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional karts for SuperTuxKart.

%description -l pl.UTF-8
Dodatkowe karty dla SuperTuxKart.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/supertuxkart/

cp -a data $RPM_BUILD_ROOT%{_datadir}/games/supertuxkart/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/supertuxkart/data/karts/*
