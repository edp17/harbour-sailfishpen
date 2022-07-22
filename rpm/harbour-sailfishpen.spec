Name:           harbour-sailfishpen
Version:        1.0.0
Release:        1
Summary:        SailfishPen is Samsung's Spen support for Galaxy Note 4.
License:        GPLv3
URL:            https://github.com/edp17/harbour-sailfishpen
Source0:        %{name}-%{version}.tar.bz2

%description
SailfisPen is inspired by Samsung's S-Pen and is created for Sailfish Os.

%prep
%setup

%install
mkdir -p %{buildroot}/usr/bin/droid
mkdir -p %{buildroot}/usr/lib/systemd/system
mkdir -p %{buildroot}/usr/share/harbour-spen-menu
mkdir -p %{buildroot}/usr/share/icons/hicolor/86x86/apps

install -D -m775 config/harbour-spen-menu %{buildroot}/usr/bin/harbour-spen-menu
install -D -m775 config/evtest %{buildroot}/usr/bin/evtest
install -D -m644 config/harbour-spen-menu.qml %{buildroot}/usr/share/harbour-spen-menu/qml/harbour-spen-menu.qml
install -D -m644 config/CoverPage.qml %{buildroot}/usr/share/harbour-spen-menu/qml/cover/CoverPage.qml
install -D -m644 config/Main.qml %{buildroot}/usr/share/harbour-spen-menu/qml/pages/Main.qml
install -D -m644 config/About.qml %{buildroot}/usr/share/harbour-spen-menu/qml/pages/About.qml
install -D -m644 config/sailfishpen.service %{buildroot}/%{_unitdir}/sailfishpen.service
install -D -m775 config/sailfishpen-daemon.sh %{buildroot}/usr/bin/droid/sailfishpen-daemon.sh
install -D -m775 config/sailfishpen-start-service.sh %{buildroot}/usr/bin/droid/sailfishpen-start-service.sh
install -D -m644 config/harbour-sailfishpen.png %{buildroot}/usr/share/icons/hicolor/86x86/apps/harbour-sailfishpen.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
systemctl daemon-reload
systemctl-user daemon-reload
systemctl enable sailfishpen

%files
%defattr(-,root,root,-)
%{_bindir}/harbour-spen-menu
%{_bindir}/evtest
%{_bindir}/droid/sailfishpen-daemon.sh
%{_bindir}/droid/sailfishpen-start-service.sh
/usr/lib/systemd/system/sailfishpen.service
%{_datadir}/harbour-spen-menu/qml/harbour-spen-menu.qml
%{_datadir}/harbour-spen-menu/qml/cover/CoverPage.qml
%{_datadir}/harbour-spen-menu/qml/pages/Main.qml
%{_datadir}/harbour-spen-menu/qml/pages/About.qml
%{_datadir}/icons/hicolor/86x86/apps/harbour-sailfishpen.png