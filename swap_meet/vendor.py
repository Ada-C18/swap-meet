from swap_meet.item import Item

class Vendor:
    '''
    object contains an attribute: inventory that is an empty list with an optional parameter
    it also contains the methods: add, remove, get_by_category, and swap_items
    '''
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        last_inventory_item = self.inventory[-1]

        return last_inventory_item

    def remove(self, item):
        for thing in self.inventory:
            if thing == item:
                self.inventory.remove(item)
                return item
        
        return False

    def get_by_category(self, category):
        item_list = []

        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        
        if item_list == []:
            return None
        
        return item_list

    def swap_items(self, other_vendor, my_item, their_item):
        '''
        swaps items between self and other inventories
        '''
        # Helpers
        self_inventory = self.inventory 
        other_inventory = other_vendor.inventory


        if my_item not in self_inventory or their_item not in other_inventory or other_inventory == [] or self_inventory ==[]:
            return False
        
        for item in self_inventory:
            if item == my_item:
                other_vendor.add(item)
                self.remove(item)

        for item in other_inventory:
            if item == their_item:
                self.add(item)
                other_vendor.remove(item)
        
        return True

    def swap_first_item(self, other_vendor):
        '''
        swaps the first items of self and other inventories
        '''
        # Helpers
        self_inventory_item = self.inventory[0]
        other_inventory_item = other_vendor.inventory[0]


        # Swap 1st items
        try:
            return self.swap_items(other_vendor, self_inventory_item, other_inventory_item)

        except:
            return False

