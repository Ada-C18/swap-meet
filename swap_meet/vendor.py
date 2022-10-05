class Vendor:
    
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
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
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, other, my_item, their_item):
        if not my_item or not their_item:
            return False
        if not my_item in self.inventory or not their_item in other.inventory:
            return False
        self.inventory.remove(my_item)
        other.inventory.append(my_item)
        self.inventory.append(their_item)
        other.inventory.remove(their_item)
        return True

    def swap_first_item(self, other):
        if not self.inventory or not other.inventory:
            return False
        return self.swap_items(other, 
                        self.inventory[0], 
                        other.inventory[0])
    
    def get_best_by_category(self, category):
        items_in_category = [item for item in self.inventory if item.category == category]
        if not items_in_category:
            return None
        return max(items_in_category, key=lambda i: i.condition)
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        if not self.inventory or not other.inventory:
            return False
        return self.swap_items(other, 
                        self.get_best_by_category(their_priority),
                        other.get_best_by_category(my_priority))
    
    def get_newest(self):
        return min(self.inventory, key=lambda i: i.age)
    
    def swap_by_newest(self, other):
        if not self.inventory or not other.inventory:
            return False
        return self.swap_items(other, self.get_newest(), other.get_newest())