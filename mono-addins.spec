Name:     	mono-addins
Version:	0.5
Release:	%mkrel 2
License:	MIT
BuildArch:      noarch
URL:		http://www.go-mono.com
Source0:	http://ftp.novell.com/pub/mono/sources/%name/%name-%version.tar.bz2
BuildRequires:	mono-devel gtk-sharp2
Summary:	Mono Addins
Group:		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mono Addin Support

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Mono Addin Support - development files and tools
	  
%prep
%setup -q

%build
./configure --prefix=%_prefix
#gw parallel make broken in 0.4
make

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
%_mandir/man1/mautil.1*
%_prefix/lib/mono/mono-addins/mautil.exe

%_prefix/lib/mono/gac/Mono.Addins
%_prefix/lib/mono/gac/policy.0.2.Mono.Addins
%_prefix/lib/mono/gac/policy.0.3.Mono.Addins
%_prefix/lib/mono/mono-addins/Mono.Addins.dll

%_prefix/lib/mono/gac/Mono.Addins.CecilReflector/
%_prefix/lib/mono/gac/policy.0.2.Mono.Addins.CecilReflector/
%_prefix/lib/mono/gac/policy.0.3.Mono.Addins.CecilReflector/
%_prefix/lib/mono/mono-addins/Mono.Addins.CecilReflector.dll

%_prefix/lib/mono/gac/Mono.Addins.Setup
%_prefix/lib/mono/gac/policy.0.2.Mono.Addins.Setup
%_prefix/lib/mono/gac/policy.0.3.Mono.Addins.Setup
%_prefix/lib/mono/mono-addins/Mono.Addins.Setup.dll

%_prefix/lib/mono/gac/Mono.Addins.Gui
%_prefix/lib/mono/gac/policy.0.2.Mono.Addins.Gui
%_prefix/lib/mono/gac/policy.0.3.Mono.Addins.Gui
%_prefix/lib/mono/gac/policy.0.4.Mono.Addins
%_prefix/lib/mono/gac/policy.0.4.Mono.Addins.CecilReflector
%_prefix/lib/mono/gac/policy.0.4.Mono.Addins.Gui
%_prefix/lib/mono/gac/policy.0.4.Mono.Addins.Setup
%_prefix/lib/mono/mono-addins/Mono.Addins.Gui.dll

%files devel
%defattr(-, root, root)
%_datadir/pkgconfig/*.pc
#gw these depend on stuff in libmono-devel:
%_prefix/lib/mono/gac/Mono.Addins.MSBuild
%_prefix/lib/mono/gac/policy.0.2.Mono.Addins.MSBuild
%_prefix/lib/mono/gac/policy.0.3.Mono.Addins.MSBuild
%_prefix/lib/mono/gac/policy.0.4.Mono.Addins.MSBuild
%_prefix/lib/mono/mono-addins/Mono.Addins.MSBuild.dll
%_prefix/lib/mono/xbuild/Mono.Addins.targets

