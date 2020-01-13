{ stdenv
, libdebian-installer
}:

stdenv.mkDerivation rec {
  pname = "debian-installer-utils";
  version = "1.133";

  src = builtins.fetchTarball {
    url = "https://deb.debian.org/debian/pool/main/d/debian-installer-utils/debian-installer-utils_${version}.tar.xz";
    # with --unpack
    sha256 = "0ycwh8akhaaq0vxdhygqlzfa55kdq24agyxisv2xz59irsl21585";
  };

  buildInputs = [
    libdebian-installer
  ];

  installPhase = ''
    mkdir -p $out/{bin,lib}
    install anna-install $out/bin
    install apt-install $out/bin
    install block-attr $out/bin
    install debconf-disconnect $out/bin
    install debconf-get $out/bin
    install debconf-set $out/bin
    install fetch-url $out/bin
    install in-target $out/bin
    install log-output $out/bin
    install register-module $out/bin
    install search-path $out/bin
    install start-shell $out/bin
    install update-dev $out/bin
    install user-params $out/bin
    install chroot-setup.sh $out/lib
  '';
}
