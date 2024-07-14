Name:           dtkcore
Version:        5.6.32
Release:        1
Summary:        Deepin tool kit core modules
License:        LGPLv3+
Group:          System/Deepin
URL:            https://github.com/linuxdeepin/dtkcore
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  qmake5
BuildRequires:  doxygen
BuildRequires:  qt5-assistant
BuildRequires:  cmake(Dtk)
#BuildRequires:  annobin
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  cmake(Qt5Help)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  gtest-devel
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(icu-uc)

%description
Deepin tool kit core modules.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcommon-devel
Requires:       qt5-qtbase-devel%{?_isa}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
