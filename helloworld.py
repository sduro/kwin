from gi.repository import Gtk, Gio

class HelloWorldApp(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="apps.test.helloworld",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.connect("activate", self.on_activate)
        
    def on_activate(self, data=None):
        window = Gtk.Window(type=Gtk.WindowType.TOPLEVEL)
        window.set_title("Gtk3 Python Example")
        window.set_border_width(24)
        label = Gtk.Label("Hello World!")
        window.add(label)
        window.show_all()
        self.add_window(window)
    
if __name__ == "__main__":
    app = HelloWorldApp()
    app.run(None)
