from Item import Item_info

class Item_vault:

    def __init__(self, item_file):
        self.item_list = []
        self.file_reader(item_file)

    def file_reader(self, item_file):
        try:
            in_file = open(item_file, "r")
            for line in in_file:
                item_match = line.strip().replace(" ", "").split(",")
                self.item_list.append(Item_info(item_match[0], item_match[1], item_match[2], item_match[3]))
        except FileNotFoundError:
            print("!This is a warning that a CSV file could not be found!")

