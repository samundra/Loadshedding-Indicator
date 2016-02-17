import sys
import json
from gi.repository import Gtk
# from gi.overrides.Gtk import Widget
from gi.repository import Notify
from gi.repository import GObject

''' A preference window for Nepal Loadshedding application '''


class PreferenceWindow(Gtk.Window):
    notify = None
    group_number = None
    configs = {}
    __gsignals__ = { 'message_send': (GObject.SIGNAL_RUN_FIRST, None, (int,)) }

    txt_np_date_field = Gtk.Entry()

    # def __init__(self):
    #     self.txt_np_date_field = Gtk.Entry()

    def __init__(self):
        self.main()

    def do_message_send(self, arg):
        # print "class method for `my_signal' called with argument", arg
        self.group_number = arg
        return self.group_number

    def main(self):
        print "Main called"
        if not Notify.init("nepal-loadshedding"):
            sys.exit (1)

        Gtk.Window.__init__(self, title="preference ...")

        self.configs = self.parse_configs()

        self.set_resizable(False)
        self.set_position(Gtk.WindowPosition.CENTER)

        table = Gtk.Table(2, 2, True)
        self.add(table)

        label = Gtk.Label('Group Number :')

        saved_group_value = str(self.configs.get("GROUP"))

        self.group_number = saved_group_value

        self.txt_np_date_field.set_name('group_number')
        self.txt_np_date_field.set_text(saved_group_value)

        btn_close = Gtk.Button(label="Close",name='close')
        btn_close.connect("clicked", self.on_btn_close)

        btn_save = Gtk.Button(label="Save",name='save')
        btn_save.connect("clicked", self.on_btn_save)

        # label
        table.attach(label, 0, 1, 0, 1)
        # entry
        table.attach(self.txt_np_date_field, 1, 2, 0, 1)
        # close button
        table.attach(btn_close, 0, 1, 1, 2)
        # save button
        table.attach(btn_save, 1, 2, 1, 2)
        
    def parse_configs(self):
        self.configs = json.load(open("config.txt"))
        return self.configs
    
    def save_configs(self, key, value):
        self.configs[key] = int(value)
        json.dump(self.configs, open("config.txt", "wb"))
        return True
                
    def on_btn_close(self, w):
        print int(self.group_number)
        self.emit("message_send", int(self.group_number))
        self.destroy()
        
    def on_btn_save(self, widget):
        self.group_number = self.txt_np_date_field.get_text()
        update_string = "Group saved succcessfully to "+self.txt_np_date_field.get_text()
        self.save_configs("GROUP", self.txt_np_date_field.get_text())
        self.update_notification_message(update_string)

    def update_notification_message(self, message):
        if self.notify is None:
            self.notify = Notify.Notification.new("Nepal Loadshedding", message, None)

        self.notify.update("Nepal Loadshedding", message, None)
        self.notify.set_timeout(100)
        self.notify.show()

if __name__ == "__main__":
    pw = PreferenceWindow()
    # pw.main()