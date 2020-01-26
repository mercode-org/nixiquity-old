{ stdenv
, kmod
, dmidecode
}:

stdenv.mkDerivation {
  pname = "laptop-detect";
  version = "0.16";

  src = ./.;

  buildPhase = ''
    # substituteAll laptop-detect.sh
  '';

  installPhase = ''
    install -D laptop-detect.sh $out/bin/laptop-detect
  '';
}
