class Vendor: 
    def __init__(self,inventory = None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item 

    def remove(self,item):
        if item not in self.inventory:
            return False 
        self.inventory.remove(item)
        return item 

    def get_by_category(self,category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:  
            friend.inventory.append(my_item)
            self.inventory.append(their_item)
            friend.inventory.remove(their_item) 
            self.inventory.remove(my_item)
            return True
        return False

