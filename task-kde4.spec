Name:           task-kde4
Version:        4.1.2
Release:        %mkrel 4
Epoch:          1
Summary:        Metapackage for KDE4
Group:          Graphical desktop/KDE
License:        GPL
Requires:       task-kde4-minimal
# Do not require the whole kdeutils4 because we do not want superkaramba, kgpg, kcron and kdessh to be installed by default
#Requires:       kdeutils4
Suggests:       kcalc
Suggests:       kcharselect
Suggests:       kdf
Suggests:       kfloppy
Suggests:       ktimer
Suggests:       kwallet
Suggests:       sweeper
Suggests:       kdenetwork4
Suggests:       pinentry-qt
Suggests:       kdepim4
Suggests:       kdeaccessibility4
Suggests:       kdegraphics4
Suggests:       kcron
# Need to be fixed with tcb before enabling it
#Requires: kuser
Suggests:       knetworkconf
Suggests:       kdeplasma-addons
Suggests:       mandriva-galaxy-data
Requires:       kwrite
Suggests:       amarok
Suggests:       kdegames4
Suggests:       digikam
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
Requires:   kdm
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
Requires:   keditbookmarks
Requires:   phonon-gstreamer
Requires:   kscd
Requires:   dragonplayer
Requires:   kdeartwork4-kscreensaver
Suggests:   task-pulseaudio
Suggests:   preload
Suggests:   readahead
Requires:   xsettings-kde

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


