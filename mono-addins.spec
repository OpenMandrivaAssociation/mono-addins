Name:     	mono-addins
Version:	0.3
Release:	%mkrel 1
License:	LGPL
BuildArch:      noarch
URL:		http://www.go-mono.com
Source0:	http://go-mono.com/sources/mono-addins/%{name}-%{version}.tar.bz2
BuildRequires:	mono-devel gtk-sharp2
Summary:	Mono Addins
Group:		Development/Other

%description
Mono Addin Support
	  
%prep
%setup -q

%build
./configure --prefix=%_prefix
%make

%install
rm -rf "$RPM_BUILD_ROOT"
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%_datadir/pkgconfig
mv $RPM_BUILD_ROOT%_prefix/lib*/pkgconfig/*.pc $RPM_BUILD_ROOT%_datadir/pkgconfig

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-, root, root)
%_bindir/mautil
%_prefix/lib/mono/mono-addins/mautil.exe

%_prefix/lib/mono/gac/Mono.Addins
%_prefix/lib/mono/gac/policy.0.2.Mono.Addins
%_prefix/lib/mono/mono-addins/Mono.Addins.dll

%_prefix/lib/mono/gac/Mono.Addins.Setup
%_prefix/lib/mono/gac/policy.0.2.Mono.Addins.Setup
%_prefix/lib/mono/mono-addins/Mono.Addins.Setup.dll

%_prefix/lib/mono/gac/Mono.Addins.Gui
%_prefix/lib/mono/gac/policy.0.2.Mono.Addins.Gui
%_prefix/lib/mono/mono-addins/Mono.Addins.Gui.dll
%_datadir/pkgconfig/*.pc

