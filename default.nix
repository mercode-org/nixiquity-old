with (import <nixpkgs> { }); (callPackage ./package.nix {
  libindicator = callPackage ./libindicator.nix {
    libido = callPackage ./libido.nix { };
  };
})
