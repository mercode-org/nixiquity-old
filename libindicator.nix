{ stdenv
, fetchbzr
, lib
, file
, pkgconfig
, autoreconfHook
, libido
, gtk3
}:

with lib;

stdenv.mkDerivation rec {
  pname = "libindicator";
  version = "0.6.3";

  src = fetchbzr {
    url = "lp:libindicator";
    rev = "539";
    sha256 = "1m9b3jsi3afvv6w8vqfiwlz2w54g5j32imf5igpkam916y4fc6bb";
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
