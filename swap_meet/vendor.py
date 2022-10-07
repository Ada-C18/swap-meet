import itertools
class Vendor:

    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        if not self.inventory:
            self.inventory = []
        self.inventory.append(item)
        return item

    def remove(self, item):
        if not item in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list

    def swap_items(self, other_vendor, my_item, other_vendor_item):
        if not my_item in self.inventory or \
            not other_vendor_item in other_vendor.inventory:
            return False
        my_item_to_swap = self.remove(my_item)
        other_vendor.add(my_item_to_swap)
        their_item_to_swap = other_vendor.remove(other_vendor_item)
        self.add(their_item_to_swap)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        my_first_item = self.inventory[0]
        other_vendor_first_item = other_vendor.inventory[0]
        return self.swap_items(other_vendor, my_first_item, \
            other_vendor_first_item)

    def get_best_by_category(self,category):
        get_category = self.get_by_category(category)
        if not get_category:
            return None
        if get_category: 
            return max(get_category, key = lambda item: item.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        best_item_they_want = self.get_best_by_category(their_priority)
        their_best_item_i_want = other.get_best_by_category(my_priority)
        if not best_item_they_want or not their_best_item_i_want:
            return False
        else:
            return self.swap_items(other, best_item_they_want,\
                their_best_item_i_want)

    def get_newest_by_age(self,age):
        get_age = self.get_by_category(age)
        if not get_age:
            return None
        if get_age: 
            return min(get_age, key = lambda item: item.age)

    # swap to get the newest items within a category
    def swap_newest_by_category(self, other_vendor, my_priority,\
        their_priority):
        newest_item_they_want = self.get_newest_by_age(their_priority)
        newest_item_i_want = other_vendor.get_newest_by_age(my_priority)
        if not newest_item_they_want or not newest_item_i_want:
            return False
        else:
            return self.swap_items(other_vendor, newest_item_they_want,\
                newest_item_i_want)