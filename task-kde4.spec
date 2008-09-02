Name:           task-kde4
Version:        4.1.1
Release:        %mkrel 1
Epoch:          1
Summary:        Metapackage for KDE4
Group:          Graphical desktop/KDE
License:        GPL
Requires:       task-kde4-minimal
# Do not require the whole kdeutils4 because we do not want superkaramba, kgpg, kcron and kdessh to be installed by default
#Requires:       kdeutils4
Requires:       kcalc
Requires:       kcharselect
Requires:       kdf
Requires:       kfloppy
Requires:       ktimer
Requires:       kwallet
Requires:       sweeper
Requires:       kdenetwork4
Suggests:       pinentry-qt
Requires:       kdepim4
Requires:       kdeaccessibility4
Requires:       kdegraphics4
Requires:       kcron
# Need to be fixed with tcb before enabling it
#Requires: kuser
Requires:       knetworkconf
Requires:       kdeplasma4
Requires:       mandriva-galaxy-data
Requires:       kwrite
Suggests:       amarok
Suggests:       kdegames4
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
Requires:   gwenview
Requires:   dolphin
Requires:   ark
Requires:   kde4-nsplugins
Requires:   kdepasswd
Requires:   konsole
Requires:   kmix
Requires:   dbus-x11
Requires:   oxygen-icon-theme
Requires:   qt4-qtdbus
Requires:   plasma-applet-folderview
Requires:   plasma-desktoptheme-aya
Requires:   plasma-applet-showdesktop
Requires:   konqueror
Requires:   phonon-gstreamer
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


