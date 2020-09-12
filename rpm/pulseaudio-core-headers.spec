%define pulsemajorminor %{expand:%(echo '%{version}' | cut -d. -f1,2)}

Name:       pulseaudio-core-headers
Summary:    PulseAudio Private Headers
Version:    13.99.1
Release:    1
Group:      Development/Libraries
License:    LGPLv2+
URL:        https://github.com/nemomobile-ux/pulseaudio-core-headers
Source0:    %{name}-%{version}.tar.xz
Source1:    pulsecore.pc.in
Requires:   pkgconfig(libpulse) >= %{pulsemajorminor}

%global debug_package %{nil}

%description
PulseAudio Core headers required by modules built out of tree.

%prep
%setup -q -n %{name}-%{version}

%build
sed -e s/@PA_MAJORMINOR@/%{pulsemajorminor}/g rpm/pulsecore.pc.in | \
    sed -e s/@ARCH_LIBDIR@/%{_libdir}/g | \
    sed -e s/@PA_FULL@/%{version}/g  > pulsecore.pc

%install
rm -rf %{buildroot}

install -Dm644 pulsecore.pc %{buildroot}/%{_libdir}/pkgconfig/pulsecore.pc

mkdir -p %{buildroot}/%{_includedir}/pulsecore/filter
mkdir -p %{buildroot}/%{_includedir}/pulsecore/ffmpeg
install -m 644 pulseaudio/src/pulsecore/*.h %{buildroot}/%{_includedir}/pulsecore
install -m 644 pulseaudio/src/pulsecore/filter/*.h %{buildroot}/%{_includedir}/pulsecore/filter
install -m 644 pulseaudio/src/pulsecore/ffmpeg/*.h %{buildroot}/%{_includedir}/pulsecore/ffmpeg

%files
%defattr(-,root,root,-)
%{_includedir}/pulsecore
%{_libdir}/pkgconfig/pulsecore.pc
