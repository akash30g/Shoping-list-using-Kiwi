from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
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
        self.root.ids.itemDisplay.clear_widgets()
        required_list = sorted(self.list, key=operator.itemgetter(2))
        self.root.ids.instructionMenu.text = "Click items to mark an item as completed"
        for each_item in required_list:
            if "r" in each_item[3]:
                if int(each_item[2]) == 1:
                    itemButton = Button(text="{} ${}".format(each_item[0], each_item[1]), background_color=[1, 0, 0, 1])
                    itemButton.item = each_item
                    #itemButton.bind(on_release=self.markCompleted)
                    self.root.ids.itemDisplay.add_widget(itemButton)
                    count += 1
                    total += float(each_item[1])
                elif int(each_item[2]) == 2:
                    itemButton = Button(text="{} ${}".format(each_item[0], each_item[1]), background_color=[0, 0, 1, 1])
                    itemButton.item = each_item
                    #itemButton.bind(on_release=self.markCompleted)
                    self.root.ids.itemDisplay.add_widget(itemButton)
                    count += 1
                    total += float(each_item[1])
                else:
                    itemButton = Button(text="{} ${}".format(each_item[0], each_item[1]), background_color=[0, 1, 0, 1])
                    itemButton.item = each_item
                    #itemButton.bind(on_release=self.markCompleted)
                    self.root.ids.itemDisplay.add_widget(itemButton)
                    count += 1
                    total += float(each_item[1])
        if count == 0:
            self.root.ids.itemInfo.text = "No required items"
            self.root.ids.itemDisplay.clear_widgets()
        else:
            self.root.ids.itemInfo.text = "Total price expected for {} items: ${}".format(count, total)

    def addItem(self):
        name = self.root.ids.item_name.text
        price = self.root.ids.item_price.text
        priority = self.root.ids.item_priority.text

        if name == "" or price == "" or priority == "":
            self.root.ids.instructionMenu.text = "All fields must be completed"
        else:
            try:
                price = float(self.root.ids.item_price.text)
                priority = int(self.root.ids.item_priority.text)
            except ValueError:
                self.root.ids.instructionMenu.text = "Please enter a valid value"
            else:
                if price <= 0:
                    self.root.ids.instructionMenu.text = "Price entered must be >= $0"
                elif priority != 1 and priority != 2 and priority != 3:
                    self.root.ids.instructionMenu.text = "Priority must be 1, 2 or 3"
                else:
                    new_item = [name, str(price), str(priority), "r"]
                    self.list.append(new_item)
                    self.root.ids.instructionMenu.text = "{}, ${} with priority {} added to shopping list".format(name, price, priority)
                    self.root.ids.input_name.text = ""
                    self.root.ids.input_price.text = ""
                    self.root.ids.input_priority.text = ""
    #def markCompleted
    # def completedListMian
    # def clearItem



    # def saveItem
    # def markCompleted

ShoppingList().run()