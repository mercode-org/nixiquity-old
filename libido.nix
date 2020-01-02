{ stdenv
, autoreconfHook
, fetchFromGitHub
, pkgconfig
, gtk3
, glib
, file
, gobject-introspection
, xorg-gtest
, vala
}:

stdenv.mkDerivation {
  pname = "libido";
  version = "12.10.2";

  src = fetchFromGitHub {
    repo = "ayatana-ido";
    owner = "AyatanaIndicators";
    rev = "0.4.90";
    sha256 = "02vqjryni96zzrpkq5d7kvgw7nf252d2fm2xq8fklvvb2vz3fa0w";
  };

  nativeBuildInputs = [
    pkgconfig
    autoreconfHook
    xorg-gtest
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
