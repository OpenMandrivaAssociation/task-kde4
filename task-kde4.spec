Name:           task-kde4
Version:        3.94.0
Release:        %mkrel 1
Epoch:          1
Summary:        Metapackage for KDE4
Group:          Graphical desktop/KDE
License:        GPL
Requires:       mandriva-kde4-config
Requires:       kdebase4
Requires:       kdebase4-workspace
Requires:       kdeplayground4-plasma
Requires:       kdelibs4-core
Requires:       kdeutils4
Requires:       kdenetwork4
Requires:       kdeaccessibility4
#Requires:       kdevelop4
#Requires:       kdeaddons4
#Requires:       kdeadmin4
Suggests:       amarok2
Suggests:       koffice2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
Obsoletes:      %{name}-full < 2008.0-3mdv

%description
This package is a meta-package, meaning that its purpose is to contain
the complete dependencies for running the KDE4 desktop ( plus Amarok2,
Koffice2, ...)

%files
%defattr(-,root,root-)

#---------------------------------------------------------------------

%package    minimal
Summary:    Minimal dependencies needed KDE4
Group:      Graphical desktop/KDE

Requires:   mandriva-kde4-config
Requires:   kdebase4-workspace
Requires:   kde4-dolphin
Requires:   kde4-nsplugins
Requires:   kde4-kdepasswd
Requires:   kde4-konsole
Requires:   kdeplayground4-plasma
Requires:   xine-phonon

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal KDE4 desktop environment.


%files minimal

#--------------------------------------------------------------------

%package devel
Summary: Metapackage for KDE development
Group: Development/KDE and Qt
Requires: mandriva-kde4-config
Requires: kdelibs4-devel
Requires: kdepimlibs4-devel
Requires: kdebase4-devel
Requires: kdebase4-workspace-devel

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for installing a KDE development environment.

%files devel
%defattr(-,root,root-)


