class Vendor:
    def __init__(self, inventory=None) -> None:
        self.inventory = inventory if inventory is not None else []

    def __str__(self, item):
        f"{self.item}"
        # return f"my_item: {self.my_item}, their_item: {self.their_item}"

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        category_list = [item for item in self.inventory if item.category == category]
        return category_list

    def swap_items(self, vendor, my_item, their_item):
        '''If this Vendor's inventory doesn't contain my_item or the friend's inventory doesn't contain their_item,
    the method returns False'''
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        self.remove(my_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        self.add(their_item)
        return True

    

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        self.inventory.append(friend.inventory[0])
        friend.inventory.append(self.inventory[0])
        self.inventory.remove(self.inventory[0])
        friend.inventory.remove(friend.inventory[0])
        return True

    def get_best_by_category(self, other, my_priority, their_priority):
        self.swap_item(other, my_priority, their_priority)

    def swap_best_by_category(self):
        pass