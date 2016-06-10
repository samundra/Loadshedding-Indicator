#!/usr/bin/python2
#^^^ not using env for process name

'''
Created on Jun 17, 2013

@author: samundra
'''

import os, sys

__filepath__ = os.path.abspath(__file__)
PWD = os.path.dirname(__filepath__) + '/'
print(PWD)

sys.path.append(PWD)

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')

from gi.repository import Gtk
from gi.repository import AppIndicator3 as AppIndicator

from nepali_calendar import NepaliDateConverter
from preference import PreferenceWindow as preference_window
from converter import ConverterWindow

import datetime
import json
import signal

import subprocess

FILE_ROUTINE = "~/.cache/routine.xml"
FILE_CONFIG  = "~/.cache/config.txt"

class LoadShedding:
    ind = None
    routines = []
    menu = None

    def __init__(self):
        self.ind = AppIndicator.Indicator.new("loadshedding-routine",
                                              # "tray-message",
                                              os.path.abspath("icon.png"),
                                              AppIndicator.IndicatorCategory.APPLICATION_STATUS)
        self.ind.set_status(AppIndicator.IndicatorStatus.ACTIVE)
        self.ind.set_attention_icon("indicator-messages-new")
        # self.ind.connect("scroll-event", self.scroll)
        self.rebuild_menu()

    def clear_menu_items(self):
        m_childrens = self.menu.get_children()
        ppos = 0;
        for c in m_childrens:
            ppos += 1
            if (ppos in [5, 6, 7]):
                self.menu.remove(c)
                c.destroy()

    def rebuild_menu(self):
        self.menu = Gtk.Menu()
        self.clear_menu_items()

        # you can use this menu item for experimenting
        item = Gtk.MenuItem()
        item.set_label("Preference")
        item.connect("activate", self.handler_menu_preference)
        item.show()
        self.menu.append(item)

        cdate = Gtk.MenuItem()
        cdate.set_label("Convert Date")
        cdate.connect("activate", self.handler_convert_date)
        cdate.show()
        self.menu.append(cdate)

        sep1 = Gtk.SeparatorMenuItem()
        sep1.show()
        self.menu.append(sep1)

        # Append the actual routine here
        self.add_dy_menu()

        # this is for exiting the app
        sep2 = Gtk.SeparatorMenuItem()
        sep2.show()
        self.menu.append(sep2)

        item = Gtk.MenuItem()
        item.set_label("Update Schedule")
        item.connect("activate", self.update_schedule)
        item.show()

        self.menu.append(item)
        self.menu.show()

        # this is for exiting the app
        sep3 = Gtk.SeparatorMenuItem()
        sep3.show()
        self.menu.append(sep3)

        item = Gtk.MenuItem()
        item.set_label("Exit")
        item.connect("activate", self.handler_menu_exit)
        item.show()

        self.menu.append(item)
        self.menu.show()

        self.ind.set_title("Menu title")
        self.ind.set_menu(self.menu)

        m_childrens = self.menu.get_children()
        print 'length ' + str(len(m_childrens))
        pos = 0;
        for c in m_childrens:
            pos += 1
            if (pos in [5, 6, 7]) and (len(m_childrens) > 9):
                self.menu.remove(c)
                c.destroy()

    def update_schedule(self, evt):
        # TODO Rewrite this to update the schedule silently in the background
        upd_string = 'cd batti && ./main.sh -u && ./main.sh -x > ../t.xml'
        #         upd_sch = subprocess.Popen(upd_string, shell=True)
        process = subprocess.Popen(upd_string, shell=True, stdout=subprocess.PIPE)
        print process.communicate()

    def handler_convert_date(self, evt):
        cd = ConverterWindow()
        cd.show_all()

    def add_dy_menu(self):
        """ Adds the dynamic menu generated from xml """
        #         now = datetime.datetime.now()
        #         labelDay = now.strftime("%Y-%m-%d")+" ("+ now.strftime("%A")+")"
        np_date_converter = NepaliDateConverter()
        np_date = np_date_converter.contents_func()
        curDate = Gtk.MenuItem(label=np_date)
        curDate.show()

        self.menu.append(curDate)

        if (self.parse_xml()):
            for items in self.routines:
                itema = Gtk.MenuItem(label=items)
                itema.show()
                self.menu.append(itema)
                # itema = None

    def get_group_number(self):
        # TODO shift it to ~/.config/loadshedding
        configs = json.load(open(os.path.expanduser(FILE_CONFIG)))
        return configs['GROUP']

    def load_routine(self, widget):
        self.parse_xml()

    def parse_xml(self):
        MY_GROUP = self.get_group_number()  # Group number
        # print MY_GROUP
        ''' Parses the routine xml and keeps the routine in memory '''
        from xml.dom import minidom

        src = os.path.expanduser(FILE_ROUTINE)
        if not os.path.isfile(src):
            os.system('batti -u && batti -x > %s'%src)

        self.xmldoc = minidom.parse(src)
        itemlist = self.xmldoc.getElementsByTagName('group')
        self.routines.append("GROUP : " + str(MY_GROUP))
        for s in itemlist:
            groupName = int(s.getAttribute('name'))

            if (groupName == MY_GROUP):
                day = s.getElementsByTagName('day')

                for dt in day:

                    dayName = dt.getAttribute('name').lower()

                    now = datetime.datetime.now()
                    currDay = now.strftime("%A").lower()

                    if (currDay == dayName):
                        self.routines.append(dt.childNodes[1].firstChild.nodeValue)
                        self.routines.append(dt.childNodes[3].firstChild.nodeValue)
                        return True
        return False

    def handler_menu_exit(self, evt):
        Gtk.main_quit()

    def handler_menu_preference(self, evt):
        pref = preference_window()
        pref.connect("message_send", self.on_pref_close)
        #         pref.connect("delete-event", Gtk.main_quit)
        pref.show_all()

    def on_pref_close(self, evt, data=None):
        self.rebuild_menu()

    def main(self):
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        Gtk.main()

    def menu_reload(self):
        print 'menu reload'


if __name__ == "__main__":
    lshd = LoadShedding()
    lshd.main()

# LoadShedding.main()
