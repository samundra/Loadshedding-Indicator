"""
Created on Jun 30, 2013

@author: samundra
"""

from gi.repository import Gtk
# from gi.overrides.Gtk import Widget
# from gi.repository import Notify
# from gi.repository import GObject
from nepali_calendar import NepaliDateConverter
from ast import literal_eval


class ConverterWindow(Gtk.Window):
    ndc = NepaliDateConverter()
    bs2ad = True
    ad2bs = False

    def __init__(self):
        Gtk.Window.__init__(self, title="Convert date")
        self.state = "off"
        self.set_resizable(False)
        self.set_position(Gtk.WindowPosition.CENTER)
        table = Gtk.Table(4, 2, True)
        self.add(table)

        # saved_group_value = "2070-02-10"
        # self.group_number = 3

        # dd = '(2070,03,16)'
        dd = str(self.ndc.today_en_date())

        self.txt_np_date_field = Gtk.Entry()
        self.txt_np_date_field.set_name('txt_np_date')
        self.txt_np_date_field.set_text("")

        self.txt_en_date_field = Gtk.Entry()
        self.txt_en_date_field.set_name('txt_en_date')
        self.txt_en_date_field.set_text(dd)

        # BS2AD or AD2BS Choices
        btn_bs_2ad = Gtk.RadioButton.new_with_label_from_widget(None, "BS2AD")
        btn_bs_2ad.connect("toggled", self.on_button_toggled, "nep_to_en")

        btn_ad_2bs = Gtk.RadioButton.new_from_widget(btn_bs_2ad)
        btn_ad_2bs.set_label("AD to BS")
        btn_ad_2bs.connect("toggled", self.on_button_toggled, "en_to_nep")
        btn_ad_2bs.set_active(True)

        btn_close = Gtk.Button(label="Close", name='close')
        btn_close.connect("clicked", self.on_btn_close)

        btn_save = Gtk.Button(label="Convert", name='Convert')
        btn_save.connect("clicked", self.on_btn_convert)

        # label
        table.attach(Gtk.Label('B.S. :'), 0, 1, 0, 1)
        # entry
        table.attach(self.txt_np_date_field, 1, 2, 0, 1)

        table.attach(Gtk.Label('A.D. :'), 0, 1, 1, 2)
        table.attach(self.txt_en_date_field, 1, 2, 1, 2)

        # Convert Dates Choices
        table.attach(btn_bs_2ad, 0, 1, 2, 3)
        table.attach(btn_ad_2bs, 1, 2, 2, 3)

        # close button
        table.attach(btn_close, 0, 1, 3, 4)
        # save button
        table.attach(btn_save, 1, 2, 3, 4)

    def on_button_toggled(self, button, name):
        if name == "nep_to_en":
            cnv_np_date = literal_eval(self.txt_np_date_field.get_text())
            self.bs2ad = True
            self.ad2bs = False
            self.txt_en_date_field.set_text(str(self.c_np_date(cnv_np_date)))
        if name == "en_to_nep":
            cnv_en_date = literal_eval(self.txt_en_date_field.get_text())
            self.ad2bs = True
            self.bs2ad = False
            self.txt_np_date_field.set_text(str(self.c_en_date(cnv_en_date)))

        if button.get_active():
            self.state = "on"
            # print "Button", name, "was turned", state

    def on_btn_close(self, w):
        # print int(self.group_number)
        # self.emit("message_send",int(self.group_number))
        self.destroy()

    def c_np_date(self, dd):
        return self.ndc.bs2ad(dd)

    def c_en_date(self, dd):
        return self.ndc.ad2bs(dd)

    def on_btn_convert(self, widget):
        if self.bs2ad:
            cnv_np_date = literal_eval(self.txt_np_date_field.get_text())
            self.txt_en_date_field.set_text(str(self.c_np_date(cnv_np_date)))
        if self.ad2bs:
            cnv_en_date = literal_eval(self.txt_en_date_field.get_text())
            self.txt_np_date_field.set_text(str(self.c_en_date(cnv_en_date)))
