{ stdenv
, autoreconfHook
, gobject-introspection
, file
, intltool
, pkgconfig
, glib
, libsoup
, networkmanager
, gnome3
, gtk3
, kdeFrameworks
, isocodes
, cairo
, iw
, gettext
, parted
, librsvg
, subunit
, libindicator
}:

/* Build-Depends: adwaita-icon-theme, apt, autopoint, bf-utf-source, check, dctrl-tools, debconf-utils, debhelper (>= 9), dh-autoreconf, dh-di (>= 3), dh-systemd, dpkg-dev (>= 1.15.7), gir1.2-nma-1.0, gir1.2-soup-2.4, gir1.2-timezonemap-1.0, gir1.2-webkit2-4.0, gir1.2-xkl-1.0, gobject-introspection, imagemagick, intltool (>= 0.40.0), intltool-debian (>= 0.30+20040212), iso-codes, isoquery, keymapper (>= 0.5.3-7), libblkid-dev, libbogl-dev, libcairo2-dev, libdebconfclient0-dev (>= 0.68), libdebian-installer4-dev (>= 0.76), libgirepository1.0-dev, libglib2.0-dev, libgtk-3-dev (>= 3.20), libindicator3-dev, libiw-dev (>= 27+28pre9), liblocale-gettext-perl, libparted-dev (>= 2.2), librsvg2-bin, libsubunit-dev, locales, pep8, pkg-config, po-debconf (>= 1.0), pyflakes3 (>= 0.7.2), python-gi-dev, python3-all (>= 3.1), python3-apt (>= 0.7.100.3~), python3-cairo, python3-dbus, python3-debconf, python3-gi, python3-gi-cairo, python3-icu (>= 1.0), python3-mock (>= 0.7.0), python3-pam, rename, scour, tzdata, ubuntu-artwork, udev, wget, xkb-data (>= 0.9), xkb-data-i18n, xvfb */

stdenv.mkDerivation {
  pname = "nixiquity";
  version = "0.0.0";

  src = ./..;

  nativeBuildInputs = [
    autoreconfHook
    file
    intltool
    pkgconfig
    gettext
    subunit
  ];

  buildInputs = [
    gtk3
    gobject-introspection
    glib
    libsoup
    networkmanager
    gnome3.webkitgtk
    kdeFrameworks.kdewebkit
    cairo
    iw
    isocodes
    parted
    librsvg
    libindicator
  ];

  autoreconfPhase = ''
    ./autogen.sh
  '';
}
