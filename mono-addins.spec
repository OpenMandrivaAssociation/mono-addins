Name:     	mono-addins
Version:	0.6.2
Release:	%mkrel 1
License:	MIT
BuildArch:      noarch
URL:		http://www.go-mono.com
Source0:	http://download.mono-project.com/sources/%name/%name-%version.tar.bz2
BuildRequires:	mono-devel gtk-sharp2
Summary:	Mono Addins
Group:		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mono Addin Support

%package 0.5
Group:		Development/Other
Summary: Mono Addins compatibility
Conflicts:	%name < 0.6-3
Requires:	%name = %version

%description 0.5
Mono Addin Support - compatibility package

%package 0.4
Group:		Development/Other
Summary: Mono Addins compatibility 
Conflicts:	%name < 0.6-3
Requires:	%name = %version

%description 0.4
Mono Addin Support - compatibility package

%package 0.3
Group:		Development/Other
Summary: Mono Addins compatibility 
Conflicts:	%name < 0.6-3
Requires:	%name = %version

%description 0.3
Mono Addin Support - compatibility package

%package 0.2
Group:		Development/Other
Summary: Mono Addins compatibility 
Conflicts:	%name < 0.6-3
Requires:	%name = %version

%description 0.2
Mono Addin Support - compatibility package

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
rm -rf "%{buildroot}"
%makeinstall_std

mkdir -p %{buildroot}%_datadir/pkgconfig
mv %{buildroot}%_prefix/lib*/pkgconfig/*.pc %{buildroot}%_datadir/pkgconfig

%clean
rm -rf "%{buildroot}"

%files
%defattr(-, root, root)
%_bindir/mautil
%_mandir/man1/mautil.1*
%_prefix/lib/mono/mono-addins/mautil.exe

%_prefix/lib/mono/gac/Mono.Addins
%_prefix/lib/mono/mono-addins/Mono.Addins.dll

%_prefix/lib/mono/gac/Mono.Addins.CecilReflector/
%_prefix/lib/mono/mono-addins/Mono.Addins.CecilReflector.dll

%_prefix/lib/mono/gac/Mono.Addins.Setup
%_prefix/lib/mono/mono-addins/Mono.Addins.Setup.dll

%_prefix/lib/mono/gac/Mono.Addins.Gui
%_prefix/lib/mono/mono-addins/Mono.Addins.Gui.dll

%files 0.2
%defattr(-, root, root)
%_prefix/lib/mono/gac/policy.0.2.Mono.Addins
%_prefix/lib/mono/gac/policy.0.2.Mono.Addins.CecilReflector/
%_prefix/lib/mono/gac/policy.0.2.Mono.Addins.Setup
%_prefix/lib/mono/gac/policy.0.2.Mono.Addins.Gui

%files 0.3
%defattr(-, root, root)
%_prefix/lib/mono/gac/policy.0.3.Mono.Addins
%_prefix/lib/mono/gac/policy.0.3.Mono.Addins.CecilReflector/
%_prefix/lib/mono/gac/policy.0.3.Mono.Addins.Setup
%_prefix/lib/mono/gac/policy.0.3.Mono.Addins.Gui

%files 0.4
%defattr(-, root, root)
%_prefix/lib/mono/gac/policy.0.4.Mono.Addins
%_prefix/lib/mono/gac/policy.0.4.Mono.Addins.CecilReflector
%_prefix/lib/mono/gac/policy.0.4.Mono.Addins.Gui
%_prefix/lib/mono/gac/policy.0.4.Mono.Addins.Setup

%files 0.5
%defattr(-, root, root)
%_prefix/lib/mono/gac/policy.0.5.Mono.Addins
%_prefix/lib/mono/gac/policy.0.5.Mono.Addins.CecilReflector/
%_prefix/lib/mono/gac/policy.0.5.Mono.Addins.Setup
%_prefix/lib/mono/gac/policy.0.5.Mono.Addins.Gui

%files devel
%defattr(-, root, root)
%_datadir/pkgconfig/*.pc
#gw these depend on stuff in libmono-devel:
%_prefix/lib/mono/gac/Mono.Addins.MSBuild
%_prefix/lib/mono/gac/policy.0.2.Mono.Addins.MSBuild
%_prefix/lib/mono/gac/policy.0.3.Mono.Addins.MSBuild
%_prefix/lib/mono/gac/policy.0.4.Mono.Addins.MSBuild
%_prefix/lib/mono/gac/policy.0.5.Mono.Addins.MSBuild
%_prefix/lib/mono/mono-addins/Mono.Addins.MSBuild.dll
%_prefix/lib/mono/xbuild/Mono.Addins.targets

