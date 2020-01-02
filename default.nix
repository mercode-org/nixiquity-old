with (import <nixpkgs> { }); (
  let
    gtk3 = callPackage ./gtk/3.x.nix {
      inherit (darwin.apple_sdk.frameworks) AppKit Cocoa;
    };
  in
    callPackage ./package.nix {
      # inherit gtk3;
      libindicator = callPackage ./libindicator.nix {
        gtk3 = gtk3;
        libido = callPackage ./libido.nix {
          gtk3 = gtk3;
          xorg-gtest = callPackage ./xorg-gtest.nix { };
        };
      };
    }
)
