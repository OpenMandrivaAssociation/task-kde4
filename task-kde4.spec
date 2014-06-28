Summary:	Metapackage for KDE4
Name:		task-kde4
Epoch:		1
Version:	4.13.2
Release:	4
Group:		Graphical desktop/KDE
License:	GPLv2

Requires:	task-kde4-minimal
Suggests:	amarok
Suggests:	bluedevil
Suggests:	kcharselect
Suggests:	kcron
Suggests:	kdenetwork4
Suggests:	plasma-nm
Suggests:	kdepim4
Suggests:	kdeplasma-addons
Suggests:	klook
Suggests:	ksnapshot
Suggests:	ktimer
Suggests:	kwallet
Requires:	gamin
Requires:	homerun
Suggests:	plasma-scriptengine-python
Suggests:	plasma-scriptengine-ruby

# These are very useful to set with GTK applications style
Suggests:	gtk-qt-engine
Suggests:	gtk-engines2
Suggests:	kde-gtk-config

BuildArch:	noarch
Obsoletes:	task-kde < 1:4.6.5
Provides:	task-kde = %{epoch}:%{version}

%description
This package is a meta-package, meaning that its purpose is to contain
the complete dependencies for running the KDE4 desktop ( plus amarok,
koffice, ...)

%files

#---------------------------------------------------------------------

%package minimal
Summary:	Minimal dependencies needed KDE4
Group:		Graphical desktop/KDE

Suggests:	task-pulseaudio
Requires:	task-x11
Requires:	distro-kde4-config-common

Suggests:	akonadi-kde
Requires:	ark
Requires:	dbus-x11
Requires:	dolphin
Requires:	gwenview

Suggests:	kamera
Suggests:	kcalc
Suggests:	kde4-audiocd
Requires:	kde4-config-file >= 2014.0
Requires:	kde4-nsplugins
Requires:	kdeartwork4-kscreensaver
Requires:	kdebase4-runtime
Requires:	kdebase4-workspace
Suggests:	kdepasswd
Requires:	kdialog
Requires:	kdm
Requires:	keditbookmarks
Suggests:	kio-sysinfo
Requires:	kickoff
Requires:	kmix
Requires:	kmozillahelper
Requires:	konsole
Requires:	kwrite

Suggests:	mandriva-galaxy
Suggests:	mandriva-galaxy-data
Suggests:	mplayerthumbs
Suggests:	okular
Suggests:	oxygen-icon-theme
Suggests:	phonon-gstreamer
Suggests:	plasma-applet-battery
Requires:	plasma-applet-showdesktop
Requires:	plasma-desktoptheme-slim-glow
Requires:	plasma-wallpaper-timeoftheday
Suggests:	preload
Requires:	qt4-qtdbus
Requires:	xsettings-kde

Obsoletes:	task-kde-minimal < 1:4.2.2
Provides:	task-kde-minimal = %{epoch}:%{version}

%description minimal
This package is a meta-package, meaning that its purpose is to contain
minimal dependencies for running a minimal KDE4 desktop environment.


%files minimal

#--------------------------------------------------------------------

%package devel
Summary:	Metapackage for KDE development
Group:		Development/KDE and Qt
Requires:	task-kde4
Requires:	kdebase4-devel
Requires:	kdebase4-workspace-devel
Requires:	kdelibs4-devel
Requires:	kdepimlibs4-devel
Requires:	kde-dev-scripts
Requires:	kde-dev-utils
Requires:	task-c++-devel

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for installing a KDE development environment.

%files devel

