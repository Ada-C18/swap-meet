from hashlib import new


class Vendor:
    
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []    
        self.inventory = inventory
    

    def add(self, item):
        self.inventory.append(item)
        return item


    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError as err:
            return False


    def get_by_category(self, category):
        return_list = []
        for item in self.inventory:
            if item.category == category:
                return_list.append(item)

        return return_list


    def swap_items(self, vendor, my_item, their_item):
        if not self.inventory or not vendor.inventory or my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            self.remove(my_item)
            vendor.remove(their_item)
            self.inventory.append(their_item)
            vendor.inventory.append(my_item)
            return True


    def swap_first_item(self, vendor):
        if self.inventory and vendor.inventory:
            self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
            return True

        return False


    def get_best_by_category(self, category):
        best_condition = 0
        best_item = None

        for item in self.inventory:
            if item.category == category:
                if item.condition > best_condition:
                    best_condition = item.condition
                    best_item = item

        return best_item


    def swap_best_by_category(self, other, my_priority, their_priority):
        #what self wants to receive from other:
        other_item = other.get_best_by_category(my_priority)

        #what other wants to receive from self
        self_item = self.get_best_by_category(their_priority)

        if other_item and self_item:
            self.swap_items(other, self_item, other_item)
            return True
        
        return False

    

    def get_newest(self):
        age = 5000000000
        newest_item = None

        for item in self.inventory:
            if item.age < age:
                age = item.age
                newest_item = item

        return newest_item


    
    def swap_by_newest(self, other):
        #what self wants to receive from other:
        others_item = other.get_newest()

        #what other wants to receive from self
        self_item = self.get_newest()

        if others_item and self_item:
            self.swap_items(other, self_item, others_item)
            return True
        
        return False