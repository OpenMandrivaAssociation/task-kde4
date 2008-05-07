Name:           task-kde4
Version:        4.0.73
Release:        %mkrel 1
Epoch:          1
Summary:        Metapackage for KDE4
Group:          Graphical desktop/KDE
License:        GPL
Requires:       task-kde4-minimal
Requires:       kdebase4
Requires:       kdelibs4-core
Requires:       kdeutils4
Requires:       kdenetwork4
Requires:       kdeaccessibility4
Requires:       kdevelop4
Requires:       kdeadmin4
Suggests:       amarok
Suggests:       koffice
Suggests:       playground-nepomuk-kde
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
Requires:   dolphin
Requires:   kde4-nsplugins
Requires:   kdepasswd
Requires:   konsole
Requires:   extragear-plasma
Requires:   phonon-xine
Requires:   dbus-x11
Suggests:   task-pulseaudio

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
Requires: kdesdk4-scripts
Requires: gcc-c++
Requires: oxygen-icon-theme

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for installing a KDE development environment.

%files devel
%defattr(-,root,root-)


