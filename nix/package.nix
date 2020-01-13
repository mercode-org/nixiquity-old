{ stdenv
, autoreconfHook
, gobject-introspection
, file
, intltool
, pkgconfig
, glib
, libsoup
, networkmanager
, gnome3
, gtk3
, kdeFrameworks
, isocodes
, cairo
, iw
, gettext
, parted
, librsvg
, subunit
, libindicator
, tzdata
, python3
, console-setup-linux
, debconf
, makeWrapper
, callPackage
, wrapGAppsHook
, pam
, python-pam
, lsb-release
, imagemagick
, networkmanagerapplet
, timezonemap
, json_glib

, frontendGtk ? true
, frontendKde ? false
, slideshowPackage ? (callPackage ./slideshow-empty.nix { })
, oemSlideshowPackage ? (callPackage ./slideshow-empty.nix { })
}:

/* Build-Depends: adwaita-icon-theme, apt, autopoint, bf-utf-source, check, dctrl-tools, debconf-utils, debhelper (>= 9), dh-autoreconf, dh-di (>= 3), dh-systemd, dpkg-dev (>= 1.15.7), gir1.2-nma-1.0, gir1.2-soup-2.4, gir1.2-timezonemap-1.0, gir1.2-webkit2-4.0, gir1.2-xkl-1.0, gobject-introspection, imagemagick, intltool (>= 0.40.0), intltool-debian (>= 0.30+20040212), iso-codes, isoquery, keymapper (>= 0.5.3-7), libblkid-dev, libbogl-dev, libcairo2-dev, libdebconfclient0-dev (>= 0.68), libdebian-installer4-dev (>= 0.76), libgirepository1.0-dev, libglib2.0-dev, libgtk-3-dev (>= 3.20), libindicator3-dev, libiw-dev (>= 27+28pre9), liblocale-gettext-perl, libparted-dev (>= 2.2), librsvg2-bin, libsubunit-dev, locales, pep8, pkg-config, po-debconf (>= 1.0), pyflakes3 (>= 0.7.2), python-gi-dev, python3-all (>= 3.1), python3-apt (>= 0.7.100.3~), python3-cairo, python3-dbus, python3-debconf, python3-gi, python3-gi-cairo, python3-icu (>= 1.0), python3-mock (>= 0.7.0), python3-pam, rename, scour, tzdata, ubuntu-artwork, udev, wget, xkb-data (>= 0.9), xkb-data-i18n, xvfb */
let
  b = b: if b then "true" else "false";
in
stdenv.mkDerivation {
  pname = "nixiquity";
  version = "0.0.0";

  src = ./..;

  nativeBuildInputs = [
    (python3.withPackages (ps: with ps; [
      pygobject3
      dbus-python
      PyICU
      python-pam
    ]))

    autoreconfHook
    file
    intltool
    pkgconfig
    gettext
    subunit
    imagemagick

    makeWrapper
    wrapGAppsHook
  ];

  buildInputs = [
    (python3.withPackages (ps: with ps; [
      pygobject3
      dbus-python
      PyICU
      python-pam
    ]))

    pam
    gtk3
    gobject-introspection
    glib
    libsoup
    networkmanager
    networkmanagerapplet # libnma
    gnome3.webkitgtk
    kdeFrameworks.kdewebkit
    cairo
    iw
    isocodes
    parted
    librsvg
    libindicator
    console-setup-linux
    debconf
    timezonemap
    json_glib
  ];

  /* makeFlags = [ "PREFIX=$(out)" ];
  configureFlags = [ "--prefix" "$(out)" ]; */

  autoreconfPhase = ''
    ./autogen.sh
    for f in {configure,m4/libtool.m4}; do
      substituteInPlace $f\
        --replace /usr/bin/file ${file}/bin/file
    done
  '';

  patchPhase = ''
    sed "s|/usr/share/xml/iso-codes|${isocodes}/share/xml/iso-codes|g" -i ./ubiquity/misc.py
    sed "s|/usr/share/xml/iso-codes|${isocodes}/share/xml/iso-codes|g" -i ./ubiquity/tz.py
    sed "s|/usr/share/zoneinfo|${tzdata}/share/zoneinfo|g" -i ./ubiquity/tz.py
    sed "s|/usr/share/console-setup|${console-setup-linux}/share/console-setup|g" -i ./ubiquity/keyboard_detector.py
    sed "s|lsb_release|${lsb-release}/bin/lsb_release|g" -i ./bin/ubiquity

    find . -type f -exec sed -i \
      -e s,/usr/share/ubiquity-slideshow,${slideshowPackage},g \
      -e s,/usr/share/oem-config-slideshow,${oemSlideshowPackage},g \
      -e s,/usr/lib/ubiquity,$out/lib/ubiquity,g \
      -e s,/usr/share/ubiquity,$out/share/ubiquity,g \
      -e s,debconf-communicate,${debconf}/bin/debconf-communicate,g \
      -e s,/usr/share/locale,/run/current-system/sw/share/locale,g \
      -e s,/usr/share/icons,/run/current-system/sw/share/icons,g \
      {} +
  '';

  postPhases = "debianInstall patchBins";

  patchBins = ''
    for b in $out/bin/ubiquity $out/bin/ubiquity-dm  $out/lib/ubiquity/bin/ubiquity; do
      patchShebangs $b
      wrapGApp $b
      wrapProgram $b \
        --prefix PYTHONPATH : "${debconf}/lib/python3/dist-packages"
    done
  '';

  # TODO: gradualy figure out what this script does and remove or enable parts of it (from debian/rules "install-stamp")

  debianInstall = ''
    convert -resize 32x32 data/ubiquity.svg pixmaps/ubiquity.xpm

    processInstallLine() {
      local files
      files=()
      local outDir

      while [ ! -z "$1" ]; do
        if [ ! -z "$2" ]; then
          files+=("$1")
        else
          outDir="$1"
        fi
        shift
      done

      if [ -z "''${files[0]}" ]; then
        files=("$outDir")
      fi

      outDir=''${outDir/"usr"/"$out"}

      mkdir -p "$outDir"
      for file in "''${files[@]}"; do
        cp -rp "$file" "$outDir/$(basename "$file")"
      done
    }

    processInstall() {
      code=$(cat "$1" | grep -v '^$' | grep -v "#" | sed "s|^|processInstallLine |g")
      set -x
      eval "$code"
      set +x
    }

    processInstall debian/ubiquity.install-any

    # set -x

    if ${b frontendGtk}; then
      processInstall debian/ubiquity-frontend-gtk.install
      # processInstallLine ubiquity/frontend/gtk_ui.py usr/lib/ubiquity/ubiquity/frontend
      # processInstallLine ubiquity/frontend/gtk_components/* usr/lib/ubiquity/ubiquity/frontend/gtk_components
      # processInstallLine gui/gtk/* usr/share/ubiquity/gtk
    fi

    if ${b frontendKde}; then
      processInstallLine ubiquity/frontend/kde_ui.py usr/lib/ubiquity/ubiquity/frontend
      processInstallLine ubiquity/frontend/kde_components/* usr/lib/ubiquity/ubiquity/frontend/kde_components
      processInstallLine gui/qt/* usr/share/ubiquity/qt
    fi

    set +x

  # dh_installdirs
  mkdir -p $out/{lib/ubiquity,}/bin
  # dh_installmenu

  # $(MAKE) install DESTDIR=`pwd`/debian/tmp

  # $(MAKE) -C d-i install

  # cp debian/ubiquity.install-any debian/ubiquity.install
  # ifneq (,$(wildcard debian/ubiquity.install-$(DEB_HOST_ARCH)))
  #  cat debian/ubiquity.install-$(DEB_HOST_ARCH) >> debian/ubiquity.install
  # endif
  # ifdef UBIQUITY_NO_GTK
  #   dh_install -Nubiquity-frontend-gtk -Noem-config-gtk
  # else
  # ifdef UBIQUITY_NO_KDE
  #   dh_install -Nubiquity-frontend-kde -Noem-config-kde
  # else
  #   dh_install
  # endif
  # endif
  # We don't need the source files installed
  # rm -rf debian/ubiquity-frontend-kde/usr/share/ubiquity/qt/images/source/

  # dh_di_numbers

  # Bits of manual installation that can't be done by dh_install

  install bin/ubiquity-wrapper $out/bin/ubiquity
  sed 's/@VERSION@/$(VERSION)/g' bin/ubiquity \
    > $out/lib/ubiquity/bin/ubiquity
  chmod +x $out/lib/ubiquity/bin/ubiquity
  # sed 's,/usr/lib/apt-setup,/usr/lib/ubiquity/apt-setup,g' \
  #   d-i/source/apt-setup/apt-setup \
  #   > $out/lib/ubiquity/apt-setup/apt-setup
  # chmod +x $out/lib/ubiquity/apt-setup/apt-setup

  # install d-i/source/apt-setup/finish-install.d/10apt-cdrom-setup \
  #   $out/lib/ubiquity/apt-setup/finish-install
  # if [ -e "d-i/source/base-installer/kernel/$(DEB_HOST_ARCH).sh" ]; then \
  #   install -m644 d-i/source/base-installer/kernel/$(DEB_HOST_ARCH).sh \
  #     $out/lib/ubiquity/base-installer/kernel.sh; \
  # fi
  # install d-i/source/clock-setup/debian/clock-setup.postinst \
  #   $out/lib/ubiquity/clock-setup/clock-setup
  # sed -e '/^# Update target system configuration/ { s/.*/exit 0/; q }' \
  #   d-i/source/clock-setup/finish-install.d/10clock-setup \
  #   > $out/lib/ubiquity/clock-setup/finish-install
  # chmod +x $out/lib/ubiquity/clock-setup/finish-install
  # sed -e 's,/usr/share/console-setup/keyboard-configuration.config,/var/lib/dpkg/info/keyboard-configuration.config,g' \
  #     -e 's,^\([[:space:]]*\)update-initramfs,\1: update-initramfs,' \
  #   d-i/source/console-setup/debian/keyboard-configuration.postinst \
  #   > $out/lib/ubiquity/console-setup/keyboard-configuration.postinst
  # (cd d-i/source/console-setup && \
  #  debian/preprocessor $(CURDIR)/$out/lib/ubiquity/console-setup/keyboard-configuration.postinst && \
  #  debian/preprocessor $(CURDIR)/$out/share/ubiquity/console-setup-apply)
  # chmod +x $out/lib/ubiquity/console-setup/keyboard-configuration.postinst
  # sed 's,\(finish_install=\).*,\1/dev/null,' \
  #    d-i/source/hw-detect/debian/hw-detect/bin/hw-detect \
  #   > debian/ubiquity/bin/hw-detect
  # chmod +x debian/ubiquity/bin/hw-detect
  # set -e; for x in languagemap localechooser; do \
  #   sed 's,/usr/share/localechooser,/usr/lib/ubiquity/localechooser,g' \
  #     d-i/source/localechooser/$$x \
  #     > $out/lib/ubiquity/localechooser/$$x; \
  #   chmod +x $out/lib/ubiquity/localechooser/$$x; \
  # done
  # cp -a d-i/source/localechooser/post-base-installer.d/05localechooser \
  #   $out/lib/ubiquity/localechooser/post-base-installer
  # patch $out/lib/ubiquity/localechooser/post-base-installer \
  #   < d-i/patches/localechooser-post-base-installer.patch
  # patch debian/ubiquity/lib/partman/finish.d/25create_swapfile \
  #   < d-i/patches/partman-swapfile-background.patch
  # chmod +x $out/lib/ubiquity/localechooser/post-base-installer
  # sed 's/\\\$${!TAB}/ /g' \
  #   $out/lib/ubiquity/localechooser/localechooser \
  #   > $out/lib/ubiquity/localechooser/localechooser-debconf
  # chmod +x $out/lib/ubiquity/localechooser/localechooser-debconf
  # install d-i/source/localechooser/finish-install.d/05localechooser \
  #   $out/lib/ubiquity/localechooser/finish-install
  # install d-i/source/tzsetup/post-base-installer.d/*tzsetup \
  #   $out/lib/ubiquity/tzsetup/post-base-installer
  # sed -e 's,/target/,/,g;s,/target,/,g' \
  #   $out/lib/ubiquity/tzsetup/post-base-installer \
  #   > debian/oem-config/usr/lib/ubiquity/tzsetup/post-base-installer-oem
  # chmod +x debian/oem-config/usr/lib/ubiquity/tzsetup/post-base-installer-oem
  # sed -i -e 's,db_input medium tzsetup/selected,db_input high tzsetup/selected,' \
  #        -e 's,/usr/share/tzsetup/tzmap,/usr/lib/ubiquity/tzsetup/tzmap,g' \
  #   $out/lib/ubiquity/tzsetup/tzsetup
  # cp $out/lib/ubiquity/user-setup/reserved-usernames \
  #   $out/lib/ubiquity/user-setup/reserved-usernames-oem
  # echo oem >> $out/lib/ubiquity/user-setup/reserved-usernames-oem
  # set -e; for x in user-setup user-setup-ask user-setup-apply; do \
  #   sed -e 's,/usr/lib/user-setup,/usr/lib/ubiquity/user-setup,g' \
  #       -e 's,/bin/sh,/bin/bash,g' \
  #     d-i/source/user-setup/$$x \
  #     > $out/lib/ubiquity/user-setup/$$x; \
  #   chmod +x $out/lib/ubiquity/user-setup/$$x; \
  # done
  # sed -i -e 's,db_input high user-setup/encrypt-home,db_input medium user-setup/encrypt-home,' \
  #   $out/lib/ubiquity/user-setup/user-setup-ask
  # sed -e 's,reserved-usernames,reserved-usernames-oem,g' \
  #   $out/lib/ubiquity/user-setup/user-setup-ask \
  #   > $out/lib/ubiquity/user-setup/user-setup-ask-oem
  # chmod +x $out/lib/ubiquity/user-setup/user-setup-ask-oem
  # install d-i/source/debian-installer-utils/list-devices-$(DEB_HOST_ARCH_OS) \
  #   debian/ubiquity/bin/list-devices
  # install d-i/source/debian-installer-utils/post-base-installer.d/10register-module \
  #   $out/lib/ubiquity/debian-installer-utils/register-module.post-base-installer
  # sed -e 's,/target/,/,g;s,/target,/,g' \
  #   d-i/source/debian-installer-utils/post-base-installer.d/10register-module \
  #   > debian/oem-config/usr/lib/ubiquity/debian-installer-utils/register-module.post-base-installer-oem
  # chmod +x debian/oem-config/usr/lib/ubiquity/debian-installer-utils/register-module.post-base-installer-oem
  # ifeq ($(DEB_HOST_ARCH),amd64)
  #   install d-i/source/shim-signed/openssl.cnf \
  #     $out/lib/ubiquity/shim-signed/openssl.cnf
  #   sed 's,/usr/lib/shim/mok/openssl.cnf,/usr/lib/ubiquity/shim-signed/openssl.cnf,g' \
  #     d-i/source/shim-signed/update-secureboot-policy \
  #     > $out/lib/ubiquity/shim-signed/update-secureboot-policy
  #   chmod +x $out/lib/ubiquity/shim-signed/update-secureboot-policy
  # endif
  '';
}
