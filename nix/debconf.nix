{ fetchgit
, stdenv
, perl
, gettext
, perlPackages
}:

stdenv.mkDerivation rec {
  pname = "debconf";
  version = "1.5.73";

  src = fetchgit {
    url = "https://salsa.debian.org/pkg-debconf/debconf.git";
    rev = "debian/${version}";
    sha256 = "1i86r4zpqrysd493n95g0m87z5l8ppr6gyj9214glcrdi37203bm";
  };

  nativeBuildInputs = [
    perl
    gettext
    perlPackages.Po4a
  ];

  patchPhase = ''
    patchShebangs doc/graph.pl
  '';

  preDistPhases = ["moveFiles"];

  moveFiles = ''
    mv $out/usr/* $out
  '';

  installFlags = ["prefix=$(out)"];
}
