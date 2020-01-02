{ stdenv
, fetchurl
, pkgconfig
, gtk3
, glib
, file
}:

stdenv.mkDerivation {
  pname = "libido";
  version = "12.10.2";

  src = fetchurl {
    url = "https://launchpad.net/ido/12.10/12.10.2/+download/ido-12.10.2.tar.gz";
    sha256 = "000zyyhm8wcww5r5xx2qqwldw9wk23gihx7qx8wf1cpf1ry9q9z2";
  };

  nativeBuildInputs = [
    pkgconfig
  ];

  buildInputs = [
    gtk3
    glib
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
