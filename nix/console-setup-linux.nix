{ stdenv
, fetchurl
, dpkg
}:

stdenv.mkDerivation rec {
  pname = "console-setup-linux";
  version = "1.194ubuntu2";

  src = fetchurl {
    url = "mirror://ubuntu/pool/main/c/console-setup/console-setup-linux_${version}_all.deb";
    sha256 = "194dnsxyrzahhibnfychpgh74ac00gdwpyk3pxrbm44z81caj45x";
  };

  nativeBuildInputs = [ dpkg ];

  unpackPhase = ''
    dpkg-deb --fsys-tarfile $src | tar xf -
  '';

  installPhase = ''
    cp -rp $PWD/usr $out
  '';
}
