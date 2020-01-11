{ config, pkgs, options, ... }:

{
  environment.etc."debconf.conf".source = "${pkgs.debconf}/etc/debconf.conf";
}
