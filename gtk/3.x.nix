{ stdenv
, fetchurl
, fetchpatch
, pkgconfig
, gettext
, docbook_xsl
, docbook_xml_dtd_43
, gtk-doc
, meson
, ninja
, python3
, makeWrapper
, shared-mime-info
, isocodes
, expat
, glib
, cairo
, pango
, gdk-pixbuf
, atk
, at-spi2-atk
, gobject-introspection
, fribidi
, xorg
, epoxy
, json-glib
, libxkbcommon
, gmp
, gnome3
, gsettings-desktop-schemas
, sassc
, x11Support ? stdenv.isLinux
, waylandSupport ? stdenv.isLinux
, mesa
, wayland
, wayland-protocols
, xineramaSupport ? stdenv.isLinux
, cupsSupport ? stdenv.isLinux
, withGtkDoc ? stdenv.isLinux
, cups ? null
, AppKit
, Cocoa
}:

assert cupsSupport -> cups != null;

with stdenv.lib;

stdenv.mkDerivation rec {
  pname = "gtk+3";
  version = "3.24.12";

  outputs = [ "out" "dev" ] ++ optional withGtkDoc "devdoc";
  outputBin = "dev";

  setupHooks = [
    ./hooks/gtk3-clean-immodules-cache.sh
    ./hooks/drop-icon-theme-cache.sh
  ];

  src = fetchurl {
    url = "mirror://gnome/sources/gtk+/${stdenv.lib.versions.majorMinor version}/gtk+-${version}.tar.xz";
    sha256 = "10xyyhlfb0yk4hglngxh2zsv9xrxkqv343df8h01dvagc6jyp10k";
  };

  patches = [
    ./patches/3.0-immodules.cache.patch
    (fetchpatch {
      name = "Xft-setting-fallback-compute-DPI-properly.patch";
      url = "https://bug757142.bugzilla-attachments.gnome.org/attachment.cgi?id=344123";
      sha256 = "0g6fhqcv8spfy3mfmxpyji93k8d4p4q4fz1v9a1c1cgcwkz41d7p";
    })
    # https://gitlab.gnome.org/GNOME/gtk/merge_requests/1002
    ./patches/01-build-Fix-path-handling-in-pkgconfig.patch

    ./ubu-patches/016_no_offscreen_widgets_grabbing.patch
    ./ubu-patches/017_no_offscreen_device_grabbing.patch
    #./ubu-patches/018_gdkenumtypes.c_location.patch
    ./ubu-patches/022_disable-viqr-im-for-vi-locale.patch
    ./ubu-patches/060_ignore-random-icons.patch
    ./ubu-patches/no-accessibility-dump.patch
    ./ubu-patches/reftest-known-fail.patch
    # ./ubu-patches/gdk-x11-Check-if-we-have-access-to-GL-before-using-G.patch
    #./ubu-patches/Force-emoji-presentation.patch
    #./ubu-patches/emojichooser-Pass-chooser-to-add_emoji.patch

    # Patches not in Debian
    ./ubu-patches/073_treeview_almost_fixed.patch
    ./ubu-patches/bzg_gtkcellrenderer_grabbing_modifier.patch
    ./ubu-patches/ubuntu_gtk_custom_menu_items.patch
    ./ubu-patches/print-dialog-show-options-of-remote-dnssd-printers.patch
    ./ubu-patches/uimanager-guard-against-nested-node-updates.patch
    ./ubu-patches/x-canonical-accel.patch
    ./ubu-patches/message-dialog-restore-traditional-look-on-unity.patch
    ./ubu-patches/0001-gtk-reftest-Force-icon-theme-to-Adwaita.patch
    #./ubu-patches/restore_filechooser_typeaheadfind.patch
    ./ubu-patches/0001-calendar-always-emit-day-selected-once.patch
    ./ubu-patches/0001-gtkwindow-set-transparent-background-color.patch
    ./ubu-patches/unity-border-radius.patch
    ./ubu-patches/unity-headerbar-maximized-mode.patch
    #./ubu-patches/gtksocket-unscale-before-sending-configurenotify.patch
    #./ubu-patches/Check-for-NULL-priv-popup_window-in-gtk_combo_box_popdown.patch
    #./ubu-patches/print-dialog-cups-check-unknown-option-values-whether-they-are-actually-custom-settings.patch

    ./headers-meson.patch
  ] ++ optionals stdenv.isDarwin [
    # X11 module requires <gio/gdesktopappinfo.h> which is not installed on Darwin
    # let’s drop that dependency in similar way to how other parts of the library do it
    # e.g. https://gitlab.gnome.org/GNOME/gtk/blob/3.24.4/gtk/gtk-launch.c#L31-33
    ./patches/3.0-darwin-x11.patch
  ];

  separateDebugInfo = stdenv.isLinux;

  mesonFlags = [
    "-Dgtk_doc=${boolToString withGtkDoc}"
    "-Dtests=false"
  ];

  # These are the defines that'd you'd get with --enable-debug=minimum (default).
  # See: https://developer.gnome.org/gtk3/stable/gtk-building.html#extra-configuration-options
  NIX_CFLAGS_COMPILE = [
    "-DG_ENABLE_DEBUG"
    "-DG_DISABLE_CAST_CHECKS"
  ];

  postPatch = ''
    files=(
      build-aux/meson/post-install.py
      demos/gtk-demo/geninclude.py
      gdk/broadway/gen-c-array.py
      gdk/gen-gdk-gresources-xml.py
      gtk/cursor/dnd-copy.png
      gtk/gen-gtk-gresources-xml.py
      gtk/gen-rc.py
      gtk/gentypefuncs.py
    )

    chmod +x ''${files[@]}
    patchShebangs ''${files[@]}
  '';

  nativeBuildInputs = [
    gettext
    gobject-introspection
    makeWrapper
    meson
    ninja
    pkgconfig
    python3
    sassc
    setupHooks
  ] ++ optionals withGtkDoc [
    docbook_xml_dtd_43
    docbook_xsl
    gtk-doc
  ];

  buildInputs = [
    libxkbcommon
    epoxy
    json-glib
    isocodes
  ]
  ++ optional stdenv.isDarwin AppKit
  ;

  propagatedBuildInputs = with xorg; [
    at-spi2-atk
    atk
    cairo
    expat
    fribidi
    gdk-pixbuf
    glib
    gsettings-desktop-schemas
    libICE
    libSM
    libXcomposite
    libXcursor
    libXi
    libXrandr
    libXrender
    pango
  ]
  ++ optional stdenv.isDarwin Cocoa  # explicitly propagated, always needed
  ++ optionals waylandSupport [ mesa wayland wayland-protocols ]
  ++ optional xineramaSupport libXinerama
  ++ optional cupsSupport cups
  ;
  #TODO: colord?

  doCheck = false; # needs X11

  postInstall = optionalString (!stdenv.isDarwin) ''
    # The updater is needed for nixos env and it's tiny.
    moveToOutput bin/gtk-update-icon-cache "$out"
    # Launcher
    moveToOutput bin/gtk-launch "$out"

    # TODO: patch glib directly
    for f in $dev/bin/gtk-encode-symbolic-svg; do
      wrapProgram $f --prefix XDG_DATA_DIRS : "${shared-mime-info}/share"
    done
  '';

  # Wrap demos
  postFixup =  optionalString (!stdenv.isDarwin) ''
    demos=(gtk3-demo gtk3-demo-application gtk3-icon-browser gtk3-widget-factory)

    for program in ''${demos[@]}; do
      wrapProgram $dev/bin/$program \
        --prefix XDG_DATA_DIRS : "$GSETTINGS_SCHEMAS_PATH:$out/share/gsettings-schemas/${pname}-${version}"
    done
  '';

  passthru = {
    updateScript = gnome3.updateScript {
      packageName = "gtk+";
      attrPath = "gtk3";
    };
  };

  meta = {
    description = "A multi-platform toolkit for creating graphical user interfaces";
    longDescription = ''
      GTK is a highly usable, feature rich toolkit for creating
      graphical user interfaces which boasts cross platform
      compatibility and an easy to use API.  GTK it is written in C,
      but has bindings to many other popular programming languages
      such as C++, Python and C# among others.  GTK is licensed
      under the GNU LGPL 2.1 allowing development of both free and
      proprietary software with GTK without any license fees or
      royalties.
    '';
    homepage = https://www.gtk.org/;
    license = licenses.lgpl2Plus;
    maintainers = with maintainers; [ raskin vcunat lethalman worldofpeace ];
    platforms = platforms.all;
  };
}
