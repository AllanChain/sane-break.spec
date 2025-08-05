Name:           sane-break
Version:        0.9.0
Release:        1
Summary:        A gentle break reminder that helps you avoid mindlessly skipping breaks
License:        GPL-3.0-or-later
URL:            https://github.com/AllanChain/sane-break
Source0:        https://github.com/AllanChain/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  qt6-qtwayland-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  layer-shell-qt-devel
BuildRequires:  qt6-linguist
BuildRequires:  wayland-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  desktop-file-utils
BuildRequires:  cmake
BuildRequires:  g++
Requires:       qt6-qtbase
Requires:       qt6-qtmultimedia
Recommends:     libXScrnSaver
Recommends:     qt6-qtwayland
Recommends:     layer-shell-qt

%description
%{summary}

%prep
%autosetup

%build
cmake .
cmake --build . --parallel

%install
cmake --install . --prefix=%{buildroot}/%{_prefix}
desktop-file-install                                    \
--delete-original                                       \
--dir=%{buildroot}%{_datadir}/applications              \
%{buildroot}/%{_datadir}/applications/io.github.AllanChain.sane-break.desktop

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/io.github.AllanChain.sane-break.desktop

%files
%{_bindir}/sane-break
%{_libdir}/sane-break/libsanebreak_idle_x11.so
%{_libdir}/sane-break/libsanebreak_idle_wayland.so
%{_libdir}/sane-break/libsanebreak_idle_gnome.so
%{_libdir}/sane-break/libsanebreak_wayland_check.so
%{_libdir}/sane-break/libsanebreak_layer_shell.so
%{_datadir}/icons/hicolor/scalable/apps/io.github.AllanChain.sane-break.svg
%{_datadir}/applications/io.github.AllanChain.sane-break.desktop
%{_datadir}/metainfo/io.github.AllanChain.sane-break.metainfo.xml
%{_datadir}/gnome-shell/extensions/sane-break@allanchain.github.io/extension.js
%{_datadir}/gnome-shell/extensions/sane-break@allanchain.github.io/metadata.json
%license LICENSE
%doc README.md

%changelog
%autochangelog
