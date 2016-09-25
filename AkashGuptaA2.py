from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
import csv
import operator
from functools import partial


class ShoppingList(App):

    def build(self):
        self.file_opener = open("item_list.csv")
        self.file_reader = csv.reader(self.file_opener)
        self.list = sorted(self.file_reader, key=operator.itemgetter(2))
        self.title = "Shopping List 2.0"
        self.root = Builder.load_file("AkashGuptaA2.kv")
        self.required_list_main()
        return self.root

    def required_list_main(self):
        count = 0
        total = 0
        self.root.ids.popup.dismiss()
        self.root.ids.itemDisplay.clear_widgets()
        required_list = sorted(self.list, key=operator.itemgetter(2))
        self.root.ids.instructionMenu.text = "Click items to mark an item as completed. Priotities: RED (1), BLUE (2) and GREEN (3)"
        for each_item in required_list:
            if "r" in each_item[3]:
                if int(each_item[2]) == 1:
                    item_button = Button(text="{} ${}".format(each_item[0], each_item[1]), background_color=[1, 0, 0, 1])
                    item_button.item = each_item
                    item_button.bind(on_press=partial(self.mark_completed, "1"))
                    self.root.ids.itemDisplay.add_widget(item_button)
                    count += 1
                    total += float(each_item[1])
                elif int(each_item[2]) == 2:
                    item_button = Button(text="{} ${}".format(each_item[0], each_item[1]), background_color=[0, 0, 1, 1])
                    item_button.item = each_item
                    item_button.bind(on_press=partial(self.mark_completed, "1"))
                    self.root.ids.itemDisplay.add_widget(item_button)
                    count += 1
                    total += float(each_item[1])
                else:
                    item_button = Button(text="{} ${}".format(each_item[0], each_item[1]), background_color=[0, 1, 0, 1])
                    item_button.item = each_item
                    item_button.bind(on_press=partial(self.mark_completed, "1"))
                    self.root.ids.itemDisplay.add_widget(item_button)
                    count += 1
                    total += float(each_item[1])
        if count == 0:
            self.root.ids.itemInfo.text = "No required items"
            self.root.ids.itemDisplay.clear_widgets()
        else:
            self.root.ids.itemInfo.text = "Total price expected for {} items: ${}".format(count, total)

    def add_item(self):
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
                    self.root.ids.item_name.text = ""
                    self.root.ids.item_price.text = ""
                    self.root.ids.item_priority.text = ""
        self.required_list_main()

    def clear_item(self):
        self.root.ids.item_name.text = ""
        self.root.ids.item_price.text = ""
        self.root.ids.item_priority.text = ""

    def completed_list_main(self):
        count = 0
        total = 0
        self.root.ids.itemDisplay.clear_widgets()
        completed_list = sorted(self.list, key=operator.itemgetter(2))
        for item in completed_list:
            if "c" in item[3]:
                item_button = Button(text="{} ${}".format(item[0], item[1]))
                item_button.item = item
                item_button.bind(on_press=partial(self.mark_completed, "2"))
                self.root.ids.itemDisplay.add_widget(item_button)
                count += 1
                total += float(item[1])
        if count == 0:
            self.root.ids.itemInfo.text = "No completed items"
            self.root.ids.itemDisplay.clear_widgets()
        else:
            self.root.ids.itemInfo.text = "Total price expected for {} items: ${}".format(count, total)

    def mark_completed(self, val, instance):
        if int(val) == 1:
            instance.item[3] = "c"
            self.required_list_main()
            self.root.ids.instructionMenu.text = "{}, ${} with priority {} is completed".format(instance.item[0], instance.item[1], instance.item[2])
        else:
            self.root.ids.instructionMenu.text = "{}, ${} with priority {} is completed".format(instance.item[0], instance.item[1], instance.item[2])

    def save_item(self):
        write_file = open("item_list.csv", "a")
        count = 0
        for item in self.list:
            if "c" in item[3]:
                count += 1
                if count == 1:
                    write_file2 = open("item_list.csv", "w")
                    write_file2.writelines(item[0] + "," + item[1] + "," + item[2] + "," + "c")
                    write_file2.close()
                else:
                    write_file.writelines("\n" + item[0] + "," + item[1] + "," + item[2] + "," + "c")
            else:
                write_file.writelines("")
        for item in self.list:
            if "r" in item[3]:
                count += 1
                if count == 1:
                    write_file2 = open("item_list.csv", "w")
                    write_file2.writelines(item[0] + "," + item[1] + "," + item[2] + "," + "r")
                    write_file2.close()
                else:
                    write_file.writelines("\n" + item[0] + "," + item[1] + "," + item[2] + "," + "r")
        if count == 0:
            file_writer2 = open("item_list.csv", "w")
            file_writer2.close()
        self.root.ids.instructionMenu.text = "{} items saved to items.csv".format(count)
        write_file.close()
        self.root.ids.popup.open()
        self.root.ids.show.text = "{} items saved to items.csv".format(count)


ShoppingList().run()
