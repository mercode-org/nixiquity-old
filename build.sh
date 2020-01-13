#!/bin/bash

if [ ! -e ../quitygit ]; then
  mv .git ../quitygit
fi
rm result
nix-build -j auto "$@"
mv ../quitygit .git
