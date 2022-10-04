class Vendor:
    
    def __init__(self, inventory=0):
        # try:
        #     self.inventory = inventory
        # except TypeError as err:
        #     self.inventory = []
       
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []
        
    

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError as err:
            return False

    def get_by_category(self, category):
        return_list = []
        for item in self.inventory:
            if item.category == category:
                return_list.append(item)

        return return_list

    def swap_items(self, vendor, my_item, their_item):
        if not self.inventory or not vendor.inventory or my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            self.remove(my_item)
            vendor.remove(their_item)
            self.inventory.append(their_item)
            vendor.inventory.append(my_item)
            return True