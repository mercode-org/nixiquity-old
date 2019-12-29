# nixiquity

A ubiquity-based NixOS installer

WIP

# Upstream & Updating

Upstream is maintained at https://code.launchpad.net/ubiquity

To update with latest upstream, do

```
git remote add upstream https://git.launchpad.net/ubiquity # once
git fetch upstream
git rebase upstream/master
```

# Todos

- [ ] generate config from user input
- [ ] remove debian releated things (chroot, etc)
- [ ] run nix commands instead:

```
nixos-generate-config --root /mnt
nixos-install --root /mnt
```

- [ ] add visual progress bar for nixos-install

