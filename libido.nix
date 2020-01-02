{ stdenv
, autoreconfHook
, fetchbzr
, pkgconfig
, gtk3
, glib
, file
, gobject-introspection
, xorg-gtest
, vala
, gnome2
}:

stdenv.mkDerivation rec {
  pname = "libido";
  version = "0.4.90";

  src = fetchbzr {
    url = "lp:ido";
    rev = "198";
    sha256 = "1z5sj3vlmk98rkjfxh7riaa64lr3wpj3ighcgpc38aq2c64maan9";
  };

  nativeBuildInputs = [
    pkgconfig
    autoreconfHook
    xorg-gtest
    gnome2.gtkdoc
  ];

  buildInputs = [
    gtk3
    glib
    gobject-introspection
    vala
  ];

  configureFlags = [
    "CFLAGS=-Wno-error"
    "--sysconfdir=/etc"
    "--localstatedir=/var"
  ];

  installFlags = [
    "sysconfdir=\${out}/etc"
    "localstatedir=\${TMPDIR}"
  ];

  preConfigure = ''
    for f in {configure,m4/libtool.m4}; do
      substituteInPlace $f\
        --replace /usr/bin/file ${file}/bin/file
    done
  '';
}
