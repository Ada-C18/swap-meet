from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item
    

    def get_by_category(self, category = ""):
        items = []
      
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

item_a = Item(category="clothing")
print(f"{item_a.category=}")
    # def swap_items(self, friend_vendor = [], my_item = Item(), their_items = ""):
    #     their_items = self.inventory.remove(my_item)
    #     friend_vendor.append(their_items)
    #     return True

        



