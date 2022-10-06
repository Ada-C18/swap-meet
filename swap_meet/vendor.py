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
        items_by_category = []
        for item in self.inventory:
            if item.category == category:
                items_by_category.append(item)
        return items_by_category

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
        return self.swap_items(friend,self.inventory[0],friend.inventory[0])
        
    def get_best_by_category(self, category):
        items_by_category = self.get_by_category(category)
        items_by_condition = []
        for item in items_by_category:
            items_by_condition.append(item.condition)
        sorted_condition = sorted(items_by_condition)
        for item in items_by_category:
            if item.condition == sorted_condition[-1]:
                return item
        return None 

    def swap_best_by_category(self, other, my_priority, their_priority):
        items_match_their_priority = self.get_by_category(their_priority)
        items_match_my_priority = other.get_by_category(my_priority)
        if not items_match_their_priority or not items_match_my_priority:
            return False

        best_item_from_self = self.get_best_by_category(their_priority)
        best_item_from_other = other.get_best_by_category(my_priority)

        return self.swap_items(other, best_item_from_self, best_item_from_other)


            
        
        

