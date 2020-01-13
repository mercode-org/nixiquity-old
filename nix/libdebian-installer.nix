{ stdenv
, autoreconfHook
, gettext
, pkgconfig
, perl
, dpkg
, check
}:

stdenv.mkDerivation rec {
  pname = "libdebian-installer";
  version = "0.120";

  src = builtins.fetchTarball {
    url = "https://deb.debian.org/debian/pool/main/libd/libdebian-installer/libdebian-installer_${version}.tar.xz";
    # with --unpack
    sha256 = "1yz4ly89mhrg7jzpr9slbzi633gwj35dy5f4qswps6jr6p9hja1k";
  };

  nativeBuildInputs = [
    autoreconfHook
    gettext
    pkgconfig
    perl
    dpkg
    check
  ];
}
