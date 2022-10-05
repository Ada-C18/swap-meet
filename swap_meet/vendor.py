from .item import Item


class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []
        
    
    def add(self, item):
    
        self.inventory.append(item)
        return item 
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item 
        return False

    def get_by_category(self, category):
        items_list = []
        for item in self.inventory:
            print(self.inventory)
            if item.category == category:
                items_list.append(item)
        return items_list
     

   #create a Vendor instance method named `swap_items:
    # create 3 attributes and parameters:
    # 1. an instance of another `Vendor`, representing the friend that the vendor is swapping with
#     2. an instance of an `Item` (`my_item`), representing the item this `Vendor` instance plans to give
#     3. an instance of an `Item` (`their_item`), representing the item the friend `Vendor` plans to give
#     4. If this `Vendor`'s inventory doesn't contain `my_item` or the friend's inventory doesn't contain `their_item:
#           return False
    # 5. if my_item is in Vendor's inventory 
    #       remove from Vendor's inventory
    #       add to friend's inventory
    # 6. if their_item in friend's inventory:
    #       remove from friend's inventory
    #       add to Vendor's inventory
    #       return True

    def swap_items(self, friend, my_item, their_item):
        self.friend = Vendor()
        self.my_item = Item()
        self.their_item = Item()
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        
        self.remove(my_item)
        friend.inventory.append(my_item)
        
        friend.inventory.remove(their_item)
        self.add(their_item)
        return True
