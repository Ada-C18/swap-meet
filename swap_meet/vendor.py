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
            # print(self.inventory)
            return item
        return False

    def get_by_category(self, category):
        # alternative solution: 
        # list_of_items = []
        # for item in self.inventory:
        #     if item.category == category:
        #         list_of_items.append(item)
        # return list_of_items

        list_of_items = [item for item in self.inventory 
        if item.category == category]
        return list_of_items

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        item_being_removed = self.remove(my_item)
        friend.add(item_being_removed)
        print(self.inventory, friend.inventory)

        item_being_removed = friend.remove(their_item)
        self.add(item_being_removed)
        print(self.inventory, friend.inventory)

        return True

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False

        item_being_removed = self.remove(self.inventory[0])
        friend.add(item_being_removed)

        item_being_removed = friend.remove(friend.inventory[0])
        self.add(item_being_removed)
        return True

    def get_best_by_category(self, category):
        best_item = Item()
        item_exists = False

        for item in self.inventory:
            if item.category == category and item.condition > best_item.condition:
                best_item = item
                item_exists = True
        
        if not item_exists:
            return None
        
        return best_item
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False

        self.swap_items(other, my_best_item, their_best_item)
        return True

        
