from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.category == category:
                result.append(item)
        return result

    def swap_items(self, other, my_item, their_item):
        if my_item not in self.inventory or their_item not in other.inventory:
            return False

        self.remove(my_item)
        other.add(my_item)
        other.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, other):
        if not self.inventory or not other.inventory:
            return False

        self_first = self.inventory.pop(0)
        another_first = other.inventory.pop(0)
        self.inventory.append(another_first)
        other.inventory.append(self_first)
        return True

    def get_best_by_category(self, category):
        # if not self.inventory:
        #     return None
        best_item = None
        highest_condition = 0

        for item in self.inventory:
            if item.category == category:
                if item.condition > highest_condition:
                    highest_condition = item.condition
                    best_item = item
        
        return best_item
    

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if not my_best:
            return False
        if not their_best:
            return False
            
        self.swap_items(other, my_best, their_best)
        return True


    def swap_by_newest(self, other):
        my_newest_aged_item = min(self.inventory, key=lambda item: item.age)
        their_newest_aged_item = min(other.inventory, key=lambda item: item.age)
        self.swap_items(other, my_newest_aged_item, their_newest_aged_item)
        return True


    




        

  










    