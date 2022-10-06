from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = None):

        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):                         
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        return [item for item in self.inventory if category == item.category]
        # items_list = []
        # for item in self.inventory:
        #     if category == item.category:
        #         items_list.append(item)
        # return items_list

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        
        self.add(their_item)
        friend.add(my_item)
        self.remove(my_item)
        friend.remove(their_item)

        return True

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        
        self.swap_items(friend, self.inventory[0], friend.inventory[0])
        return True

    def get_best_by_category(self, category):
        best_category = self.get_by_category(category)
        if not best_category:
            return None 
        
        best_condition = best_category[0]
        
        for item in best_category:
            if item.condition > best_condition.condition:
                best_condition = item
        
        return best_condition 

    def swap_best_by_category(self,other, my_priority, their_priority):
        self_best_category = self.get_best_by_category(their_priority)
        their_best_category = other.get_best_by_category(my_priority)
        
        if not self_best_category or not their_best_category:
            return False
    
        self.swap_items(other, self_best_category, their_best_category)
        return True