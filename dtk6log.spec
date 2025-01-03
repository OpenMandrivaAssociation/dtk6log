Name:           dtk6log
Version:        0.0.1
Release:        2
Summary:        Deepin tool kit core modules
License:        LGPLv3+
Group:          System/Deepin
URL:            https://github.com/linuxdeepin/dtk6log
Source0:        https://github.com/linuxdeepin/dtk6log/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  qmake5
BuildRequires:  cmake(Dtk)
#BuildRequires:  annobin
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  cmake(Qt5Help)
BuildRequires:  cmake(spdlog)

%description
Deepin tool kit core modules.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcommon-devel

%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1

%build
%cmake
%make_build

%install
%make_install -C build

%libpackages

cat >>%{specpartsdir}/%{mklibname -d dtklog}.specpart <<EOF
%{_includedir}/dtk5
%{_libdir}/cmake/DtkLog
%{_libdir}/qt5/mkspecs/modules/qt_lib_dtklog.pri
EOF
