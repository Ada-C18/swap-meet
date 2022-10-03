


class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []
        
    
    def add(self, item):
    
        self.inventory.append(item)
        return item 
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item 
        return False

    def get_by_category(self, category):
        items_list = []
        for item in self.inventory:
            print(self.inventory)
            if item.category == category:
                items_list.append(item)
        return items_list

# Instances of `Vendor` have an instance method named `swap_items`
#   - It takes 3 arguments:
#     1. an instance of another `Vendor`, representing the friend that the vendor is swapping with
#     2. an instance of an `Item` (`my_item`), representing the item this `Vendor` instance plans to give
#     3. an instance of an `Item` (`their_item`), representing the item the friend `Vendor` plans to give
#   - It removes the `my_item` from this `Vendor`'s inventory, and adds it to the friend's inventory
#   - It removes the `their_item` from the other `Vendor`'s inventory, and adds it to this `Vendor`'s inventory
#   - It returns `True`
#   - If this `Vendor`'s inventory doesn't contain `my_item` or the friend's inventory doesn't contain `their_item`, the method returns `False`

    # def swap_items(self, )