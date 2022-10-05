class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.item = item
        self.inventory.append(self.item)
        return self.item

    def remove(self, item):
        self.item = item
        if self.item not in self.inventory:
            return False
        else:
            self.inventory.remove(self.item)
            return self.item

    def get_by_category(self, category):
        items_filtered_by_category = []   

        for item in self.inventory:
            if item.category == category:
                items_filtered_by_category.append(item)

        return items_filtered_by_category

            
    def swap_items(self, friend, my_item, their_item):

        if my_item in self.inventory and their_item in friend.inventory:             
            self.remove(my_item)
            self.add(their_item)

            friend.remove(their_item)
            friend.add(my_item)

            return True
        return False
            

        
    def swap_first_item(self, friend):

        if len(self.inventory) != 0 and len(friend.inventory) != 0:

            my_first_item = self.inventory[0]
            their_first_item = friend.inventory[0]
            
            return self.swap_items(friend, my_first_item, their_first_item)
        return False



vendor1 = Vendor([])