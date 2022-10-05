class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item
        
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category=""):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        self.inventory.remove(my_item)
        friend.inventory.append(my_item)
        friend.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True


    def swap_first_item(self, friend):
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False
        
        self.inventory.append(friend.inventory[0])
        friend.inventory.append(self.inventory[0])
        self.inventory.remove(self.inventory[0])
        friend.inventory.remove(friend.inventory[0])
        return True
        
    def get_best_by_category(self, category):
        items_by_category = self.get_by_category(category)
        items_by_condition = []
        for item in items_by_category:
            items_by_condition.append(item.condition)
        sorted_condition = sorted(items_by_condition)
        for item in items_by_category:
            if item.condition == sorted_condition[-1] and item.category == category:
                return item
        return None 

    def swap_best_by_category(self, other, my_priority, their_priority):
        items_by_category = self.get_by_category(their_priority)
        items_by_condition = []
        for item in items_by_category:
            items_by_condition.append(item.condition)
        sorted_condition = sorted(items_by_condition)

        other_items_category = other.get_by_category(my_priority)
        other_items_by_condition = []

        for item in other_items_category:
            other_items_by_condition.append(item.condition)
        sorted_other_condition = sorted(other_items_by_condition)
        for item in self.inventory:
            if not item.category in self.inventory == their_priority:
                return False
        for item in other.inventory:
            if not item.category in other.inventory == my_priority:
                return False
    
            self.inventory.append(sorted_other_condition[-1])
            other.inventory.append(sorted_condition[-1])
            self.inventory.remove(sorted_condition[-1])
            other.inventory.remove(sorted_other_condition[-1])

            
        
        

