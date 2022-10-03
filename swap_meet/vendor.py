# import swap_meet.item
class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False

        self.inventory.remove(item) #is .remove the real thing to use?
        
        return item

    def get_by_category(self, a_category):
        self.a_category: a_category
        items = []
        for item in self.inventory:
            if item.category == a_category:
                items.append(item)
        return items
    
    def swap_items(self, friend, my_item, their_item):
        self.friend = friend
        self.my_item = my_item
        self.their_item = their_item
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        else:    
            self.remove(my_item)
            friend.add(my_item)
            
            friend.remove(their_item)
            self.add(their_item)
            return True