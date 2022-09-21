import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
win.set_default_size(185, 80)

fixed = Gtk.Fixed()
win.add(fixed)

label = Gtk.Label()
label.set_text("Name:")

entry = Gtk.Entry()
button = Gtk.Button(label="show")

def show(widget):
    print(entry.get_text())
    entry.set_text("")

button.connect("clicked", show)

fixed.put(label, 10, 0)
fixed.put(entry, 10, 25)
fixed.put(button, 115, 75)

win.show_all()

Gtk.main()
