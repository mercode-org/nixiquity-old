{ stdenv,
  autoreconfHook
}:

stdenv.mkDerivation {
  pname = "nixiquity";
  version = "0.0.0";

  src = ./.;

  nativeBuildInputs = [
    autoreconfHook
  ];
}
