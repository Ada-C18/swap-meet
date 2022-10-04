
from unicodedata import category


class Vendor:
     # inventory (list of items)
    # accept item class instances

    def __init__(self, inventory=None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if not item in self.inventory:
            return False
        else:
            self.inventory.remove(item) #explore other removal methods
            return item
    
    def get_by_category(self, category):
        items_list = []
        for element in self.inventory:
            if element.category == category:
                items_list.append(element)

        return items_list

    def swap_items(self,vendor2,item1,item2):
        #print(f"Vendor 1:{self.inventory}, Vendor 2:{vendor2.inventory}")
        if item1 in self.inventory and item2 in vendor2.inventory:
            self.inventory.remove(item1)
            vendor2.inventory.remove(item2)
            vendor2.inventory.append(item1)
            self.inventory.append(item2)
            
            return True
        #print(f"Vendor 1:{self.inventory}, Vendor 2:{vendor2.inventory}")
        else:
            return False
    
    def swap_first_item(self, vendor2):
        if not self.inventory or not vendor2.inventory:
            return False
        else:
            self_item = self.inventory[0]
            friend_item = vendor2.inventory[0]
            self.inventory[0] = friend_item
            vendor2.inventory[0] = self_item
            return True
    
    def get_best_by_category(self, category):

        return(max(self.get_by_category(category), key=lambda item: item.condition, default=None))

    def swap_best_by_category():
        pass