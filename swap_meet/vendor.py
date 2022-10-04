# from swap_meet.item import Item
class Vendor:
    
    def __init__(self,inventory=None):
        self.inventory = inventory if inventory is not None else []


    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):

        return [item for item in self.inventory if category == item.category]

    def swap_items(self,friend, my_item, their_item):

        if my_item in self.inventory and their_item in friend.inventory:
            self.inventory.remove(my_item)
            friend.inventory.remove(their_item)
            self.inventory.append(their_item)
            friend.inventory.append(my_item)
            return True
        return False

        
    def swap_first_item(self, friend):
        vendor_item = self.inventory
        friend_item = friend.inventory
        
        if self.inventory and friend.inventory:
            vendor_item = self.inventory.pop(0)
            friend_item = friend.inventory.pop(0)
            self.inventory.append(friend_item)
            friend.inventory.append(vendor_item)
            return True
        return False

