from swap_meet.item import Item

class Vendor:
    
    def __init__(self, inventory= None):
        self.inventory = inventory if inventory is not None else []
        
# default list error here (inventory= None)

    def add(self, item):
        self.inventory.append(item)
        return item 
        
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
    
    def get_by_category(self, category):
        self.inventory.append(category)
        return self.inventory 
        
    def get_by_category(self, category):
        list_of_category_match = []
        for i in self.inventory:
            if i.category == category:
                list_of_category_match.append(i)
        return list_of_category_match
        
    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
            
        friend.add(my_item)
        self.remove(my_item)
        
        friend.remove(their_item)
        self.add(their_item)
        
        return True

    def swap_first_item(self, friend):
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False
        
        my_first_item = self.inventory[0]
        friend_first_item = friend.inventory[0]
        
        self.remove(my_first_item)
        self.add(friend_first_item)

        friend.remove(friend_first_item)
        friend.add(my_first_item)

        return True
    
    def get_best_by_category(self, category = ""):
        max_condition = 0
        best_item = None
        for i in self.inventory:
            if i.category == category and i.condition > max_condition:
                max_condition = i.condition
                best_item = i

        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        if not self.get_by_category(their_priority) or not other.get_by_category(my_priority):
            return False

        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        other.add(my_best_item)
        self.remove(my_best_item)

        self.add(their_best_item)
        other.remove(their_best_item)

        return True

"""



    - If the `Vendor` has no item that matches `their_priority` category, swapping does not happen, and it returns `False`
    - If `other` has no item that matches `my_priority` category, swapping does not happen, and it returns `False`       

"""