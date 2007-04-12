Name: task-kde4
Version: 1.0
Release: %mkrel 1
Summary: Metapackage for KDE4
Summary(pt_BR): Metapacote para o KDE4
Summary(es): Metapackage for the KDE4
Group: Graphical desktop/KDE
Packager:       Mandriva Linux KDE Team <kde@mandriva.com>
License: GPL
Requires: 	kdebase4-progs 
Requires:	kdelibs4
Requires:	kdeutils4
Requires:	kdeadmin4
Requires:	kdenetwork4
Requires:	kdeaddons4
Requires:	kdevelop4
Requires:	kdeaccessibility4
Requires:	kdepimlibs4
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
This package is a meta-package, meaning that its purpose is to contain
dependencies for running the K Desktop Environment.

%description -l pt_BR
Este pacote é um metapacote, ou seja, o seu único propósito é conter
dependências para permitir executar o K Desktop Environment.

%package devel
Summary: Metapackage for KDE development
Summary(pt_BR): Metapacote para os pacotes básicos de desenvolvimento do KDE 
Summary(es): Metapackage for the KDE4 base devel
Group: Development/KDE and Qt
Requires: kdelibs4-devel

%description devel
This package is a meta-package, meaning that its purpose is to contain
dependencies for installing a KDE development environment.

%description -l pt_BR devel
Este pacote é um metapacote, ou seja, o seu único propósito é conter
dependências para instalar um ambiente de desenvolvimento do KDE.

%files
%defattr(-,root,root-)

%files devel
%defattr(-,root,root-)



