#!/usr/bin/env python3
import subprocess
import gi.repository
gi.require_version('Budgie', '1.0')
from gi.repository import Budgie, GObject, Gtk

class SomeApp(GObject.GObject, Budgie.Plugin):

    __gtype_name__ = "SomeApp"

    def __int__(self):
        GObject.Object.__init__(self)

    def do_get_panel_widget(self, uuid):
        return SomeAppApplet(uuid)


class SomeAppApplet(Budgie.Applet):

    manager = None

    def __init__(self, uuid):

        Budgie.Applet.__init__(self)

        self.box = Gtk.EventBox()
        self.add(self.box)
        img = Gtk.Image.new_from_icon_name("firefox", Gtk.IconSize.MENU)
        self.box.add(img)
        self.menu = Gtk.Menu()
        self.create_menu()
        self.box.show_all()
        self.show_all()

    def scale100(self, menuitem):
        print(menuitem)
        subprocess.Popen(["scale100.sh"])

    def scale90(self, menuitem):
        print(menuitem)
        subprocess.Popen(["scale90.sh"])

    def create_menu(self):
        item1 = Gtk.MenuItem('100%')
        item1.connect("activate", self.scale100)
        item2 = Gtk.MenuItem('90%')
        item2.connect("activate", self.scale90)
        item3 = Gtk.MenuItem('Test')
        for item in [item1, item2, item3]:
            self.menu.append(item)
        self.menu.show_all()
        self.box.connect("button-press-event", self.popup_menu)

    def popup_menu(self, *args):
        self.menu.popup(
            None, None, None, None, 0, Gtk.get_current_event_time()
        )
