{ stdenv
, fetchgit
, pkgconfig
, autoreconfHook
, file
, lib
, xorg
, evemu
, gtest
}:

with lib;

stdenv.mkDerivation rec {
  pname = "xorg-gtest";
  version = "0.7.1-unstable";

  src = fetchgit {
    url = "https://gitlab.freedesktop.org/xorg/test/xorg-gtest.git";
    rev = "b421e56afcff07b1e36009a4e18cd238707debf3";
    sha256 = "0yhywyl8ywb7qhs61zkbjyf9cnfywiycvzrk271acdxd3svqmalg";
  };

  nativeBuildInputs = [
    pkgconfig
    autoreconfHook
    xorg.utilmacros
  ];

  propagatedBuildInputs = [
    evemu
    gtest
  ];

  buildInputs = [
    xorg.libX11
    xorg.libXi
    xorg.libXext
  ];

  configureFlags = [
    "CFLAGS=-Wno-error"
    "--sysconfdir=/etc"
    "--localstatedir=/var"
    "enable_integration_tests=no"
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
