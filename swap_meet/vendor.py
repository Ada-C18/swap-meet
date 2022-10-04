from swap_meet.item import Item
class Vendor:

    def __init__(self,inventory = []):
        
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
        list_items =[]

        for item in self.inventory:
            if item.category == category:
                list_items.append(item)

        return list_items   


    def swap_items(self,friend,my_item,their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            friend.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            friend.remove(their_item)
            return True
        return False 

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory :
            return False
        self.swap_items(friend, self.inventory[0],friend.inventory[0])
        return True       






        