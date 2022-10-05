from sre_constants import CATEGORY_LINEBREAK


class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]

    def swap_items(self, vendor1, my_item, their_item):
        # vendor1 = Vendor() Ask an instructor why you dont have to create an instance this way
        # clean this function up
        if my_item in self.inventory and their_item in vendor1.inventory:
            self.add(their_item)
            self.remove(my_item)
            vendor1.add(my_item)
            vendor1.remove(their_item)
            return True
        return False

    def swap_first_item(self, vendor1):
        if not self.inventory or not vendor1.inventory:
            return False
        my_first_item = self.inventory[0]
        friend_first_item = vendor1.inventory[0]
        return self.swap_items(vendor1, my_first_item, friend_first_item)

    # def get_best_by_category(self, category):
    #     items = [item for item in self.inventory if item.category == category]

    #     for ele in items:
    #         if ele == category:

        # best_match = self.get_by_category(category)
        # best_match = None
        # return best_match
        # if best_match:
        #     for item in category:
        #         if item > best_condition_item:
        #             best_condition_item = item
        #     return best_condition_item
        # find the max condition in find category
        # then return the name of the item with highest condition
    #     if best_match in self.inventory:

    #     item_list = []
    #     for item in best_match:
    #         item_list.append(item)
        

    #     best_cat = max(item_list, key=condition)
    #     return best_cat


    # def swap_best_by_category(self, other, my_priority, their_priority):
    #     my_best_item = self.swap_best_by_category(their_priority)
    #     their_best_item = other.swap_best_by_category(my_priority)
    #     if my_best_item and their_best_item:
    #         return True
    #     return False


