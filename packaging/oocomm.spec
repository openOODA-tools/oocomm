Name:           oocomm
Version:        0.1.0
Release:        1%{?dist}
Summary:        Compares two sorted files line by line to produce unique and common lines.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oocomm
Source0:        oocomm-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oocomm is a sovereign, capability-bounded LINE INTERSECTOR written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oocomm
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oocomm-uninstall

%files
/usr/bin/oocomm
/usr/bin/oocomm-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
