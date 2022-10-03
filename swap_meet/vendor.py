from swap_meet.item import Item
class Vendor:
    
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category = ""):
        self.item_in_category_list = []
        for item in self.inventory:
            if item.category == category:
                print("made it")
                self.item_in_category_list.append(item)
        return self.item_in_category_list

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.add(their_item)
            friend.remove(their_item)
            friend.add(my_item)
            self.remove(my_item)
            return True
        return False