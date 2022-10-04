from swap_meet.item import Item

class Vendor:
    '''
    object contains an attribute: inventory that is an empty list with an optional parameter
    it also contains the methods: add, remove, get_by_category, swap_items, and swap_first_item
    '''
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        '''
        adds item parameter to self.inventory
        '''
        self.inventory.append(item)
        last_inventory_item = self.inventory[-1]

        return last_inventory_item

    def remove(self, item):
        '''
        removes item parameter from self.inventory
        '''
        for product in self.inventory:
            if product == item:
                self.inventory.remove(item)
                return item
        
        return False

    def get_by_category(self, category):
        '''
        appends items from inventory that match the category parameter
        '''
        item_list = []

        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        
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
        # Swap 1st items
        try:
            # Helpers
            self_inventory_item = self.inventory[0]
            other_inventory_item = other_vendor.inventory[0]
            return self.swap_items(other_vendor, self_inventory_item, other_inventory_item)

        except:
            return False

