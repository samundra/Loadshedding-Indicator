'''
Created on Jun 30, 2013

@author: samundra
'''

from gi.repository import Gtk
from gi.overrides.Gtk import Widget
from gi.repository import Notify
from gi.repository import GObject
from nepali_calendar import NepaliDateConverter
from ast import literal_eval

class ConverterWindow(Gtk.Window):
    ndc = NepaliDateConverter()
    bs2ad = True
    ad2bs = False
    def __init__(self):
        Gtk.Window.__init__(self, title="Convert date")
        self.set_resizable(False)
        self.set_position(Gtk.WindowPosition.CENTER)
        table = Gtk.Table(4, 2, True)
        self.add(table)

        #saved_group_value = "2070-02-10"
        #self.group_number = 3
        
        #dd = '(2070,03,16)'
        dd = str(self.ndc.today_en_date())
        
        self.txtNpDateField = Gtk.Entry()
        self.txtNpDateField.set_name('txt_np_date')
        self.txtNpDateField.set_text("")
        
        self.txtEnDateField = Gtk.Entry()
        self.txtEnDateField.set_name('txt_en_date')
        self.txtEnDateField.set_text(dd)
        
        #BS2AD or AD2BS Choices
        btnBs2Ad = Gtk.RadioButton.new_with_label_from_widget(None, "BS2AD")
        btnBs2Ad.connect("toggled", self.on_button_toggled, "nep_to_en")
        
        btnAd2Bs = Gtk.RadioButton.new_from_widget(btnBs2Ad)
        btnAd2Bs.set_label("AD to BS")
        btnAd2Bs.connect("toggled", self.on_button_toggled, "en_to_nep")
        btnAd2Bs.set_active(True)
        
        btnClose = Gtk.Button(label="Close",name='close')
        btnClose.connect("clicked", self.on_btn_close)
        
        btnSave = Gtk.Button(label="Convert",name='Convert')
        btnSave.connect("clicked", self.on_btn_convert)
        
        #label
        table.attach(Gtk.Label('B.S. :'),0,1,0,1)
        #entry
        table.attach(self.txtNpDateField,1,2,0,1)
        
        table.attach(Gtk.Label('A.D. :'),0,1,1,2)
        table.attach(self.txtEnDateField,1,2,1,2)
        
        #Convert Dates Choices
        table.attach(btnBs2Ad,0,1,2,3)
        table.attach(btnAd2Bs,1,2,2,3)
        
        #close button
        table.attach(btnClose,0,1,3,4)
        #save button
        table.attach(btnSave,1,2,3,4)
        
    def on_button_toggled(self, button, name):
        if(name=="nep_to_en"):
            cnv_np_date = literal_eval(self.txtNpDateField.get_text())
            self.bs2ad = True
            self.ad2bs = False
            self.txtEnDateField.set_text(str(self.c_np_date(cnv_np_date)))
        if(name=="en_to_nep"):
            cnv_en_date = literal_eval(self.txtEnDateField.get_text())
            self.ad2bs = True
            self.bs2ad = False
            self.txtNpDateField.set_text(str(self.c_en_date(cnv_en_date)))
            
        if button.get_active():
            state = "on"
        else:
            state = "off"
        #print "Button", name, "was turned", state
    
    def on_btn_close(self,w):
        #print int(self.group_number)
        #self.emit("message_send",int(self.group_number))
        self.destroy()
        
    def c_np_date(self,dd):
        return self.ndc.bs2ad(dd)
    
    def c_en_date(self,dd):
        return self.ndc.ad2bs(dd)
    
    def on_btn_convert(self,widget):
        if(self.bs2ad== True):
            cnv_np_date = literal_eval(self.txtNpDateField.get_text())
            self.txtEnDateField.set_text(str(self.c_np_date(cnv_np_date)))
        if(self.ad2bs==True):
            cnv_en_date = literal_eval(self.txtEnDateField.get_text())
            self.txtNpDateField.set_text(str(self.c_en_date(cnv_en_date)))

# win = ConverterWindow()
# win.connect("delete-event", Gtk.main_quit)
# win.show_all()
# Gtk.main()    