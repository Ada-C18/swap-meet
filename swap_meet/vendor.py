class Vendor:
    
    def __init__(self, inventory = None):
        self.inventory = inventory
        if not inventory:
            self.inventory = []
        

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            if not item in self.inventory:
                return False
            self.inventory.remove(item)
            return item
        except SyntaxError as err:
            print("Please enter a valid item")

    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list


    # def swap_items(self, vendor, my_item, their_item):
    #     remove my_item from self.inventory
    #     append my_item to vendor.inventory

    #     remove their_item from vendor.inventory
    #     append their_item to self.inventory

    #     returns True
    #     if vendor.inventory not have my_item 
    #     or vendor.inventory not have their_item
    #     return False


