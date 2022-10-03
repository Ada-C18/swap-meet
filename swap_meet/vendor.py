from swap_meet.item import Item

class Vendor:
    def __init__(self,inventory = []):
        self.inventory = inventory
    
    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_category(self,category = ""):
        list = []
        
        for item in self.inventory:
            if item.category == category:
                list.append(item)
        return list
    
    
    def swap_items(self,friend,my_item,their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        else:

            # self.inventory.append(their_item)
            # self.inventory.remove(my_item)
            # friend.inventory.append(my_item)
            # friend.inventory.remove(their_item)
            self.add(their_item)
            friend.add(my_item)
            self.remove(my_item)
            friend.remove(their_item)
            return True
        # if True:
        #     self.inventory.add(their_item)
        #     friend.inventory.add(my_item)
        #     self.inventory.remove(my_item)
        #     friend.inventory.remove(their_item)
        #     return True
        # else:
        #     return False