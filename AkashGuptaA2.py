from kivy.app import App
from kivy.lang import Builder
from kivy.uix.listview import ListItemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.listadapter import ListAdapter
from AkashGuptaA1 import *
import csv
import operator

class Itemlist(App):
    def build(self):
        self.file_opener = open("item_list.csv")
        self.file_reader = csv.reader(self.file_opener)
        self.list = sorted(self.file_reader, key=operator.itemgetter(2))
        self.title = "Shopping List 2.0"
        self.root = Builder.load_file("AkashGuptaA2.kv")
        return self.root