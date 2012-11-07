#!/usr/bin/python3

from gi.repository import Gtk

from ubiquity.plugin_manager import load_plugin
import sys

# we could use this as the base for the MockController as well
#   from ubiquity.frontend.base import Controller

# to test for real:
#   - qemu create -f qcow2 random-image 80G
#   - get a VM and boot with 
#     kvm -snapshot -hda random-image -cdrom quantal-desktop.iso -boot d -m 1600
# Run:
"""
sudo apt-get install bzr 
bzr co --lightweight lp:~mvo/ubiquity/ssologin
cd ssologin
sudo cp ubiquity/plugins/* /usr/lib/ubiquity/plugins && sudo cp gui/gtk/*.ui /usr/share/ubiquity/gtk && sudo ./bin/ubiquity
"""

class MockController(object):

    def __init__(self, parent):
        self.parent = parent
        self.oem_user_config = None
        self.oem_config = None
        self.dbfilter = None
        self._allow_go_foward = True
        self._allow_go_backward = True

    def add_builder(self, builder):
        pass

    def allow_go_forward(self, v):
        self._allow_go_forward = v
        self.parent.button_next.set_sensitive(v)

    def allow_go_backward(self, v):
        self._allow_go_backward = v
        self.parent.button_back.set_sensitive(v)

if __name__ == "__main__":
    """
    UBIQUITY_PLUGIN_PATH=./ubiquity/plugins/ \
    UBIQUITY_GLADE=./gui/gtk \
    ./plugin-viewer-gtk.py ubi-ubuntuone
    """
    plugin_name = sys.argv[1]
    plugin_module = load_plugin(plugin_name)

    win = Gtk.Window()
    win.button_next = Gtk.Button("next")
    win.button_back = Gtk.Button("back")

    mock_controller = MockController(win)
    page_gtk = plugin_module.PageGtk(mock_controller)


    win.button_next.connect(
        "clicked", lambda b: page_gtk.plugin_on_next_clicked())
    win.button_back.connect(
        "clicked", lambda b: page_gtk.plugin_on_back_clicked())

    button_box = Gtk.ButtonBox(spacing=12)
    button_box.set_layout(Gtk.ButtonBoxStyle.END)
    button_box.pack_start(win.button_back, True, True, 6)
    button_box.pack_start(win.button_next, True, True, 6)

    box = Gtk.VBox()
    box.pack_start(page_gtk.page, True, True, 6)
    box.pack_start(button_box, True, True, 6)

    win.add(box)
    win.connect("destroy", Gtk.main_quit)
    win.show_all()

    Gtk.main()
