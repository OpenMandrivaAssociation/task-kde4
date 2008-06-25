Name:           task-kde4
Version:        4.0.83
Release:        %mkrel 2
Epoch:          1
Summary:        Metapackage for KDE4
Group:          Graphical desktop/KDE
License:        GPL
Requires:       task-kde4-minimal
Requires:       kdeutils4
Requires:       kdenetwork4
Requires:       kdepim4
Requires:       kdeaccessibility4
Requires:       kdegraphics4
Requires:       kdegames4
Requires:       kdeutils4
Requires:       kdeadmin4
Requires:       kdeplasma4
Suggests:       amarok
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

Requires:   kde4-config-file
Requires:   kdebase4-runtime
Requires:   kdebase4-workspace
Requires:   dolphin
Requires:   kde4-nsplugins
Requires:   kdepasswd
Requires:   konsole
Requires:   dbus-x11
Requires:   oxygen-icon-theme
Requires:   qt4-qtdbus
Requires:   plasma-applet-folderview
Requires:   plasma-desktoptheme-aya
Suggests:   task-pulseaudio

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal KDE4 desktop environment.


%files minimal

#--------------------------------------------------------------------

%package devel
Summary: Metapackage for KDE development
Group: Development/KDE and Qt
Requires: task-kde4
Requires: kde4-config-file
Requires: kdelibs4-devel
Requires: kdepimlibs4-devel
Requires: kdebase4-devel
Requires: kdebase4-workspace-devel
Requires: kdesdk4-scripts
Requires: task-c++-devel

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for installing a KDE development environment.

%files devel
%defattr(-,root,root-)


