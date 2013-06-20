'''
Created on Jun 17, 2013

@author: samundra
'''
from gi.repository import Gtk
from gi.overrides.Gtk import Widget
from nepali_calendar import NepaliDateConverter
from gi.repository import AppIndicator3 as AppIndicator
from preference import PreferenceWindow
import datetime
import json
from xml.dom.minidom import parseString
 
class LoadShedding:
    ind = None
    routines = []
    menu = None
    
    def __init__(self):
        self.ind = AppIndicator.Indicator.new("loadshedding-routine", 
                                              "tray-message", 
                                              AppIndicator.IndicatorCategory.APPLICATION_STATUS)
        self.ind.set_status(AppIndicator.IndicatorStatus.ACTIVE)
        self.ind.set_attention_icon("indicator-messages-new")
        
        self.reload_menu();
        # have to give indicator a menu
    def reload_menu(self):
        
        self.menu = Gtk.Menu()

        # you can use this menu item for experimenting
        item = Gtk.MenuItem()
        item.set_label("Preference")
        item.connect("activate", self.handler_menu_preference)
        item.show()
        self.menu.append(item)

        sep1 = Gtk.SeparatorMenuItem()
        sep1.show()
        self.menu.append(sep1)
        self.add_dy_menu()
        
        # this is for exiting the app
        sep2 = Gtk.SeparatorMenuItem()
        sep2.show()
        self.menu.append(sep2)
        
        item = Gtk.MenuItem()
        item.set_label("Exit")
        item.connect("activate", self.handler_menu_exit)
        item.show()
        self.menu.append(item)
        self.menu.show()
        self.ind.set_title("Menu title")
        self.ind.set_menu(self.menu)
        
    ''' Adds the dynamic menu generated from xml '''    
    def add_dy_menu(self):
#         now = datetime.datetime.now()
#         labelDay = now.strftime("%Y-%m-%d")+" ("+ now.strftime("%A")+")"
        np_date_converter = NepaliDateConverter()
        np_date = np_date_converter.contents_func()
        curDate = Gtk.MenuItem(label=np_date)
        curDate.show()
        self.menu.append(curDate)

        if(self.parse_xml()):
            for items in self.routines:                
                item = Gtk.MenuItem(label=items)
                item.show()
                self.menu.append(item)
                
    def get_group_number(self):
        configs = json.load(open("config.txt"))
        return configs['GROUP']
    
    def load_routine(self, widget):
        self.parse_xml()
    
    def parse_xml(self):
        MY_GROUP = self.get_group_number()  # Group number
        #print MY_GROUP
        ''' Parses the routine xml and keeps the routine in memory '''
        from xml.dom import minidom
        
        self.xmldoc = minidom.parse('routine.xml')
        itemlist = self.xmldoc.getElementsByTagName('group') 
        self.routines.append("GROUP : "+str(MY_GROUP))
        for s in itemlist :
            groupName = int(s.getAttribute('name'))
            
            if(groupName==MY_GROUP):
                day = s.getElementsByTagName('day')
                
                for dt in day:

                    dayName = dt.getAttribute('name').lower()
                    
                    now = datetime.datetime.now()
                    currDay = now.strftime("%A").lower()

                    if(currDay==dayName):
                        self.routines.append(dt.childNodes[1].firstChild.nodeValue)
                        self.routines.append(dt.childNodes[3].firstChild.nodeValue)
                        return True 
        return False
                
    def handler_menu_exit(self, evt):
        Gtk.main_quit()
                
    def handler_menu_preference(self, evt):
        pref = PreferenceWindow()
        pref.connect("message_send",self.on_pref_close)
#         pref.connect("delete-event", Gtk.main_quit)
        pref.show_all()
        
    def on_pref_close(self,evt,data=None):
        print 'reloading menu'
        group_number = data
        self.reload_menu()
        
    def main(self):
        Gtk.main()
    
    def menu_reload(self):
        print 'menu reload'

if __name__ == "__main__":
    lshd = LoadShedding()
    lshd.main()

#LoadShedding.main()       
