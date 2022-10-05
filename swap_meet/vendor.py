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
        self.swap_items(friend, self.inventory[0],friend.inventory[0])
        return True

    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        if not category_list:
            return None
        return max(category_list, key=lambda x: x.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        vendor_wants = other.get_best_by_category(my_priority)
        other_wants = self.get_best_by_category(their_priority)

        if not vendor_wants or not other_wants:
            return False
        
        self.swap_items(other, other_wants, vendor_wants)
        return True

    def swap_by_newest(self, other, my_priority,their_priority):
        # Our logic is the user would say what category they want, 
        # and then swap the newest item in that category
        my_newest_list = self.get_by_category(my_priority)
        other_newest_list = other.get_by_category(their_priority)

        if not my_newest_list or not other_newest_list:
            return None
        
        my_newest_list.sort(key = lambda x:x.newest)
        other_newest_list.sort(key = lambda x:x.newest)

        self.swap(other,other_newest_list[0], my_newest_list[0])
        return True


        