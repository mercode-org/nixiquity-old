{ stdenv
, autoreconfHook
, gobject-introspection
, file
, intltool
, glib
}:

stdenv.mkDerivation {
  pname = "nixiquity";
  version = "0.0.0";

  src = ./.;

  nativeBuildInputs = [
    autoreconfHook
    file
    intltool
  ];

  buildInputs = [
    gobject-introspection
    glib
  ];

  autoreconfPhase = ''
    ./autogen.sh
  '';
}
