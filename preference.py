#import json
#import pynotify
import sys
import json
from gi.repository import Gtk
from gi.overrides.Gtk import Widget
from gi.repository import Notify
from gi.repository import GObject

class MyObject(GObject.GObject):
    __gsignals__ = {'my_signal': (GObject.SIGNAL_RUN_FIRST, None,(int,))}

    def do_my_signal(self, arg):
        print "class method for `my_signal' called with argument", arg    
    

        
''' A preference window for Nepal Loadshedding application '''
class PreferenceWindow(Gtk.Window):
    notify = None
    configs = {}
    group_number = None
    __gsignals__ = {
                    'message_send': (GObject.SIGNAL_RUN_FIRST, None,
                                      (int,))
    }
    
    def do_message_send(self, arg):
#         print "class method for `my_signal' called with argument", arg
        self.group_number = arg
        return self.group_number
        
    def __init__(self):
        if not Notify.init("nepal-loadshedding"):
            sys.exit (1)
            
        self.configs = self.parse_configs() 
        
        Gtk.Window.__init__(self, title="preference ...")
        self.set_resizable(False)
        self.set_position(Gtk.WindowPosition.CENTER)

        table = Gtk.Table(2, 2, True)
        self.add(table)

        label = Gtk.Label('Group Number :')
        
        saved_group_value = str(self.configs.get("GROUP"))
        
        self.group_number = saved_group_value
        
        self.txtEntry = Gtk.Entry()
        self.txtEntry.set_name('group_number')
        self.txtEntry.set_text(saved_group_value)
        
        btnClose = Gtk.Button(label="Close",name='close')
        btnClose.connect("clicked", self.on_btn_close)
        
        btnSave = Gtk.Button(label="Save",name='save')
        btnSave.connect("clicked", self.on_btn_save)
        
        #label
        table.attach(label,0,1,0,1)
        #entry
        table.attach(self.txtEntry,1,2,0,1)
        #close button
        table.attach(btnClose,0,1,1,2)
        #save button
        table.attach(btnSave,1,2,1,2)        
    
    def parse_configs(self):
        self.configs = json.load(open("config.txt"))
        return self.configs
    
    def save_configs(self, key, value):
        self.configs[key] = int(value)
        json.dump(self.configs, open("config.txt", "wb"))
        return True
                
    def on_btn_close(self,w):
        print int(self.group_number)
        self.emit("message_send",int(self.group_number))
        self.destroy()
        
    def on_btn_save(self,widget):
        self.group_number = self.txtEntry.get_text()
        update_string = "Group saved succcessfully to "+self.txtEntry.get_text()
        self.save_configs("GROUP", self.txtEntry.get_text())
        if(self.notify==None):
            self.notify = Notify.Notification.new("Nepal Loadshedding",update_string,None)
        self.notify.update("Nepal Loadshedding",update_string,None)
        self.notify.set_timeout(100)
        self.notify.show()
#         table.attach(button1, 0, 1, 0, 1)
#         table.attach(button2, 1, 3, 0, 1)
#         table.attach(button3, 0, 1, 1, 3)
#         table.attach(button4, 1, 3, 1, 2)
#         table.attach(button5, 1, 2, 2, 3)
#         table.attach(button6, 2, 3, 2, 3)

# win = PreferenceWindow()
# win.connect("delete-event", Gtk.main_quit)
# win.show_all()
# Gtk.main()