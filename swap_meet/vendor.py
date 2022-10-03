from swap_meet.item import Item

class Vendor:
    
    def __init__(self, inventory= None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item  
        return None

    def get_by_category(self, category):
        things_in_category = []
        for thing in self.inventory:
            if thing.category == category:
                things_in_category.append(thing)
        return things_in_category
    
    def swap_items(self, vendor_2, item_1, item_2):
        if item_1 in self.inventory and item_2 in vendor_2.inventory:
        # take first item from first vendor and give to other
            self.inventory.remove(item_1)
            vendor_2.inventory.append(item_1)
        # take second item from second vendor and give to other
            vendor_2.inventory.remove(item_2)
            self.inventory.append(item_2)
            return True
        return False

    def swap_first_item(self, other_vendor):
        if self.inventory == [] or other_vendor.inventory == []:
            return False
        else:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True
            
            # self.add(other_vendor.inventory[0])
            # other_vendor.remove(other_vendor.inventory[0])

<<<<<<< HEAD
            return True

    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)

        the_best = None
        the_best_score = 0
        if len(items_in_category) == 0:
            return the_best
        for thing in items_in_category:
            if thing.condition > the_best_score:
                the_best = thing
                the_best_score = thing.condition
        
        return the_best

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)

        if my_best == None or their_best == None:
            return False
        else:
            self.swap_items(other, my_best, their_best)
            return True

=======
            # other_vendor.add(self.inventory[0])
            # self.remove(self.inventory[0])
>>>>>>> 2b6d6e61417a78fa293766c3d95a2264d64abb34
