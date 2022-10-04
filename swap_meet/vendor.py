class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item) 
        return item
    
    def remove(self, item):
        matching_item = item
        if item not in self.inventory:
            return False
        self.inventory.remove(matching_item)
        return matching_item
        

    def get_by_category(self, category):
        inventory_list = self.inventory
        result_list = []

        for item in inventory_list:
            if item.category == category:
                result_list.append(item)
        return result_list

    def swap_items(self, friends_vendor, my_item, their_item):
        self.inventory.remove(my_item)
        friends_vendor

    