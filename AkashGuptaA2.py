from kivy.app import App  # Import relevant kivy function
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.listview import ListItemButton
from kivy.uix.boxlayout import BoxLayout
from kivy.adapters.listadapter import ListAdapter
import csv
import operator

class ShoppingList(App):
    def build(self):
        self.file_opener = open("item_list.csv")
        self.file_reader = csv.reader(self.file_opener)
        self.list = sorted(self.file_reader, key=operator.itemgetter(2))
        self.title = "Shopping List 2.0"
        self.root = Builder.load_file("AkashGuptaA2.kv")
        self.requiredListMain()
        return self.root

    def requiredListMain(self):
        count = 0
        total = 0
        self.root.ids.entriesBox.clear_widgets()
        required_list = sorted(self.list, key=operator.itemgetter(2))
        self.root.ids.status_label.text = "Click items to mark an item as completed"
        for each_item in required_list:
            if "r" in each_item[3]:
                if int(each_item[2]) == 1:
                    itemButton = Button(text="{} ${}".format(each_item[0], each_item[1]), background_color=[1, 0, 0, 1])
                    itemButton.item = each_item
                    itemButton.bind(on_release=self.markCompleted)
                    self.root.ids.entriesBox.add_widget(itemButton)
                    count += 1
                    total += float(each_item[1])
                elif int(each_item[2]) == 2:
                    itemButton = Button(text="{} ${}".format(each_item[0], each_item[1]), background_color=[0, 0, 1, 1])
                    itemButton.item = each_item
                    itemButton.bind(on_release=self.markCompleted)
                    self.root.ids.entriesBox.add_widget(itemButton)
                    count += 1
                    total += float(each_item[1])
                else:
                    itemButton = Button(text="{} ${}".format(each_item[0], each_item[1]), background_color=[0, 1, 0, 1])
                    itemButton.item = each_item
                    itemButton.bind(on_release=self.markCompleted)
                    self.root.ids.entriesBox.add_widget(itemButton)
                    count += 1
                    total += float(each_item[1])
        if count == 0:
            self.root.ids.top_label.text = "No required items"
            self.root.ids.entriesBox.clear_widgets()
        else:
            self.root.ids.top_label.text = "Total price expected for {} items: ${}".format(count, total)


    #def markCompleted
    # def completedListMian
    # def clearItem
    # def addItem
    # def saveItem
    # def markCompleted

ShoppingList().run()