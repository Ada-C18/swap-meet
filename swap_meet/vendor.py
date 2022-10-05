from swap_meet.item import Item

class Vendor:
    """creates a vendor object with an attribute called "inventory" and 2 methods: 
    "add" that adds items to the inventory, and 
    "remove" that removes item from the inventory."""
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        
    def add(self, item):
        """adds given item to the inventory. Returns the item that was added."""
        if isinstance(item, Item) or Item(item):
            self.inventory.append(item)
        elif isinstance(item, list) and len(item) == 1:
            try:
                item = Item(item[0])
                self.inventory.append(item)
                return item
            except ValueError:
                raise ValueError ("invalid type: {item}")
        elif isinstance(item, list) and len(item) > 1:
            for each_item in item:
                try:
                    each_item = Item(each_item)
                    self.inventory.append(each_item)
                except ValueError:
                    raise ValueError("invalid type: {each_item}")  
        else:
            raise ValueError("invalid type: {item}")
        return item

    def remove(self, item):
        """removes given item from the inventory. Returns the item that was removed.
        If the inventory doesn't contain that item, returns False"""
        try: 
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self, category):
        """returns the item that matches given category."""
        output_list = []
        for item in self.inventory:
            if item.category == category:
                output_list.append(item)
        return output_list
    
    def swap_items(self, friend, my_item, their_item):
        """swap one item between the current vendor object and their friends"""
        if my_item in self.inventory and their_item in friend.inventory:
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            self.add(their_item)
            return True
        return False



    

    

    


    