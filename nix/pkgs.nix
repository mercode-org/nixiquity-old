pkgs:
with pkgs;
rec {
  gtk3 = callPackage ../gtk/3.x.nix {
    inherit (darwin.apple_sdk.frameworks) AppKit Cocoa;
  };
  xorg-gtest = callPackage ./xorg-gtest.nix { };
  debconf = callPackage ./debconf.nix { };
  console-setup-linux = callPackage ./console-setup-linux.nix { };
  python-pam = python3Packages.callPackage ./python-pam.nix { };
  libido = callPackage ./libido.nix {
    inherit xorg-gtest gtk3;
  };
  libindicator = callPackage ./libindicator.nix {
    inherit libido gtk3;
  };
  nixiquity = callPackage ./package.nix {
    inherit libindicator console-setup-linux debconf python-pam gtk3;
  };
}
