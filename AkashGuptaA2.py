from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
import csv
import operator
from functools import partial

"""
Author: Akash Gupta

GiT: https://github.com/akash30g/AkashGuptaA2

Detail:
       This program runs as a GUI. It reads the items from item_list.csv. the program displays the item in color codes
        based on priorities. Clicking on the items will be marked as completed and completed items can be seen by
        completed button. User can also add the item in the required list and on closing the program all the completed
        items required items will be saved.
"""


class ShoppingList(App):                                                # main class to run the app

    def build(self):                                                    # function defined to  open file and build program
        self.file_opener = open("item_list.csv")                        # open the file
        self.file_reader = csv.reader(self.file_opener)                 # put items in a file to a list
        self.list = sorted(self.file_reader, key=operator.itemgetter(2))  # sort the items
        self.title = "Shopping List 2.0"                                # putting title for gui file
        self.root = Builder.load_file("AkashGuptaA2.kv")                # loading gui file by importing kv code
        self.required_list_main()                                       # calling function to display contents
        return self.root

    def required_list_main(self):
        count = 0
        total = 0
        self.root.ids.popup.dismiss()                                   # will be used later to dismiss pop up
        self.root.ids.itemDisplay.clear_widgets()                       # clear everything
        required_list = sorted(self.list, key=operator.itemgetter(2))   # sort the items and out items in required_list
        self.root.ids.instructionMenu.text = "Click items to mark an item as completed. Priotities: RED (1), BLUE (2) and GREEN (3)"  # sending text to a bottom label
        for each_item in required_list:             # for every item in list
            if "r" in each_item[3]:
                if int(each_item[2]) == 1:          # checks priority
                    item_button = Button(text="{} ${}".format(each_item[0], each_item[1]), background_color=[1, 0, 0, 1])  #for giving background color based on priority and creating button
                    item_button.item = each_item
                    item_button.bind(on_press=partial(self.mark_completed, "1"))  # assigning function to a button and using partial tp pass object and a value
                    self.root.ids.itemDisplay.add_widget(item_button)   # adding button to the widget
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
            self.root.ids.itemInfo.text = "No required items"       # if no items are there sending this text to label
            self.root.ids.itemDisplay.clear_widgets()               # clearing label in a widget
        else:
            self.root.ids.itemInfo.text = "Total price expected for {} items: ${}".format(count, total)     # sending instruction to label

    def add_item(self):                                                 # function defined to add the item
        name = self.root.ids.item_name.text                             # getting name from input
        price = self.root.ids.item_price.text                           # getting price from input
        priority = self.root.ids.item_priority.text                     # getting priority from input

        if name == "" or price == "" or priority == "":
            self.root.ids.instructionMenu.text = "All fields must be completed"   # validating user input as all fields must be filled
        else:
            try:                                    # validating user input for price and priority
                price = float(self.root.ids.item_price.text)
                priority = int(self.root.ids.item_priority.text)
            except ValueError:
                self.root.ids.instructionMenu.text = "Please enter a valid value"  # user should enter a valid value and this will change the label
            else:
                if price <= 0:
                    self.root.ids.instructionMenu.text = "Price entered must be >= $0"
                elif priority != 1 and priority != 2 and priority != 3:
                    self.root.ids.instructionMenu.text = "Priority must be 1, 2 or 3"
                else:
                    new_item = [name, str(price), str(priority), "r"]
                    self.list.append(new_item)  # adding new item in a the main list
                    self.root.ids.instructionMenu.text = "{}, ${} with priority {} added to shopping list".format(name, price, priority)
                    self.root.ids.item_name.text = ""  # clearing the text boxes for next user entry
                    self.root.ids.item_price.text = ""
                    self.root.ids.item_priority.text = ""
        self.required_list_main()   # calling function to see the added item

    def clear_item(self):     # defining the function to clear text boxes after pressing the button
        self.root.ids.item_name.text = ""   # clearing the text boxes for next user entry
        self.root.ids.item_price.text = ""
        self.root.ids.item_priority.text = ""

    def completed_list_main(self):    # defining the function to show completed list after pressing the button
        count = 0
        total = 0
        self.root.ids.itemDisplay.clear_widgets()  # clearing the field
        completed_list = sorted(self.list, key=operator.itemgetter(2))   # sorting the list
        for item in completed_list:    # for every item in the list
            if "c" in item[3]:      # looking for "c" in the list
                item_button = Button(text="{} ${}".format(item[0], item[1]))
                item_button.item = item
                item_button.bind(on_press=partial(self.mark_completed, "2"))   # assigning function to a button and using partial tp pass object and a value
                self.root.ids.itemDisplay.add_widget(item_button)
                count += 1
                total += float(item[1])
        if count == 0:
            self.root.ids.itemInfo.text = "No completed items"    # displaying label if there is no items
            self.root.ids.itemDisplay.clear_widgets()
        else:
            self.root.ids.itemInfo.text = "Total price expected for {} items: ${}".format(count, total)

    def mark_completed(self, val, instance):     # defining the function to handle the bottom label
        if int(val) == 1:
            instance.item[3] = "c"          # if the value passed is 1, the "r" in the list will be changed to c
            self.required_list_main()
            self.root.ids.instructionMenu.text = "{}, ${} with priority {} is marked completed".format(instance.item[0], instance.item[1], instance.item[2])
        else:
            self.root.ids.instructionMenu.text = "{}, ${} with priority {} is completed".format(instance.item[0], instance.item[1], instance.item[2])

    def save_item(self):                    # defining the function the the save the item in csv file
        write_file = open("item_list.csv", "a")     # opening the file to add items
        count = 0
        for item in self.list:          # for every item in list that has "c" in it
            if "c" in item[3]:
                count += 1
                if count == 1:
                    write_file2 = open("item_list.csv", "w")        # opening the file and writing completed item into it
                    write_file2.writelines(item[0] + "," + item[1] + "," + item[2] + "," + "c")
                    write_file2.close()         # closing the file
                else:
                    write_file.writelines("\n" + item[0] + "," + item[1] + "," + item[2] + "," + "c")
            else:
                write_file.writelines("")
        for item in self.list:
            if "r" in item[3]:      # for every item in list that has "c" in it
                count += 1
                if count == 1:
                    write_file2 = open("item_list.csv", "w")        # opening the file and writing completed item into it
                    write_file2.writelines(item[0] + "," + item[1] + "," + item[2] + "," + "r")
                    write_file2.close()
                else:
                    write_file.writelines("\n" + item[0] + "," + item[1] + "," + item[2] + "," + "r")
        if count == 0:
            file_writer2 = open("item_list.csv", "w")
            file_writer2.close()
        self.root.ids.instructionMenu.text = "{} items saved to items.csv".format(count)        # telling user via bottom label how many items has been saved
        write_file.close()
        self.root.ids.popup.open()          # opening a pop up window if user press save and exit
        self.root.ids.show.text = "{} items saved to items.csv".format(count)   # showing the text in pop up window


ShoppingList().run()  # start the program
