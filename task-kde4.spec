Name:           task-kde4
Version:        4.6.0
Release:        %mkrel 1
Epoch:          1
Summary:        Metapackage for KDE4
Group:          Graphical desktop/KDE
License:        GPL
Requires:       task-kde4-minimal
Suggests:       kcharselect
Suggests:       ktimer
Suggests:       kwallet
Suggests:       kdenetwork4
Suggests:       kdepim4
Suggests:       kdeaccessibility4
Suggests:       kdegraphics4
Suggests:       kcron
Suggests:       kdeplasma-addons
Suggests:       kdegames4
Suggests:       clementine
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
Obsoletes:      %{name}-full < 2008.0-3mdv
Obsoletes:      task-kde < 1:4.2.2
Provides:       task-kde = %epoch:%version
Obsoletes:      task-kde3 < 3.5.10-5

%description
This package is a meta-package, meaning that its purpose is to contain
the complete dependencies for running the KDE4 desktop ( plus amarok,
koffice, ...)

%files
%defattr(-,root,root-)

#---------------------------------------------------------------------

%package    minimal
Summary:    Minimal dependencies needed KDE4
Group:      Graphical desktop/KDE

Requires:   task-x11
Requires:   kde4-config-file
Requires:   kdm
Requires:   kdebase4-runtime
Requires:   kdebase4-workspace
Requires:   gwenview
Requires:   dolphin
Requires:   ark
Requires:   kde4-nsplugins
Suggests:   kdepasswd
Requires:   konsole
Requires:   kmix
Requires:   dbus-x11
Suggests:   oxygen-icon-theme
Requires:   qt4-qtdbus
Requires:   plasma-applet-folderview
Requires:   plasma-desktoptheme-aya
Requires:   plasma-applet-showdesktop
Requires:   konqueror
Requires:   keditbookmarks
Requires:   kdialog
Suggests:   phonon-gstreamer
Suggests:   dragonplayer
Requires:   kdeartwork4-kscreensaver
Requires:   xsettings-kde
Suggests:   task-pulseaudio
Suggests:   preload
Suggests:   readahead
Suggests:   kde4-audiocd
Suggests:   plasma-applet-battery
Suggests:   okular
Suggests:   plasma-applet-yawp
Suggests:   drakconf
Suggests:   mandriva-galaxy
Suggests:   akonadi-kde
Suggests:   kontact
Suggests:   konq-plugins
Suggests:   mplayerthumb
Suggests:   kamera
Requires:   kmozillahelper
Suggests:   kcalc
Requires:   plasma-wallpaper-timeoftheday
Suggests:   digikam
Suggests:   kde4-irc-client
Suggests:   kio-sysinfo
Suggests:   nepomuk-scribo
Suggests:   mandriva-galaxy-data
Requires:   kwrite
Suggests:   gtk-qt-engine
Obsoletes:  task-kde-minimal < 1:4.2.2
Provides:   task-kde-minimal = %epoch:%version

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal KDE4 desktop environment.


%files minimal

#--------------------------------------------------------------------

%package   devel
Summary:   Metapackage for KDE development
Group:     Development/KDE and Qt
Requires:  task-kde4
Requires:  kde4-config-file
Requires:  kdelibs4-devel
Requires:  kdepimlibs4-devel
Requires:  kdebase4-devel
Requires:  kdebase4-workspace-devel
Requires:  kdesdk4-scripts
Requires:  task-c++-devel
Obsoletes: task-kde-devel < 1:4.2.2
Obsoletes: task-kde3-devel < 3.5.10-5

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for installing a KDE development environment.

%files devel
%defattr(-,root,root-)


