{ stdenv
, fetchFromGitHub
, lib
, file
, pkgconfig
, autoreconfHook
, libido
, gtk3
}:

with lib;

stdenv.mkDerivation rec {
  pname = "libayatana-indicator";
  version = "0.6.3";

  src = fetchFromGitHub {
    repo = "libayatana-indicator";
    owner = "AyatanaIndicators";
    rev = version;
    sha256 = "1q9wmaw6pckwyrv0s7wkqzm1yrk031pbz4xbr8cwn75ixqyfcb28";
  };

  nativeBuildInputs = [
    pkgconfig
    autoreconfHook
  ];

  buildInputs = [
    gtk3
    libido
  ];

  preConfigure = ''
    substituteInPlace configure \
      --replace 'LIBINDICATOR_LIBS+="$LIBM"' 'LIBINDICATOR_LIBS+=" $LIBM"'
    for f in {build-aux/ltmain.sh,configure,m4/libtool.m4}; do
      substituteInPlace $f\
        --replace /usr/bin/file ${file}/bin/file
    done
  '';

  configureFlags = [
    "CFLAGS=-Wno-error"
    "--sysconfdir=/etc"
    "--localstatedir=/var"
  ];

  installFlags = [
    "sysconfdir=\${out}/etc"
    "localstatedir=\${TMPDIR}"
  ];

  doCheck = false; # fails 8 out of 8 tests

  meta = {
    description = "A set of symbols and convenience functions for Ayatana indicators";
    homepage = https://launchpad.net/libindicator;
    license = licenses.gpl3;
    platforms = platforms.linux;
    maintainers = [ maintainers.msteen ];
  };
}
