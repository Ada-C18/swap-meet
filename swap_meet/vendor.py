from operator import truediv


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
        inventory_list = self.inventory
        
        if my_item not in inventory_list or their_item not in friends_vendor.inventory:
            return False

        # print([item.category for item in inventory_list])
        # print([item.category for item in friends_vendor.inventory])
        swap_happened = False
        for item in inventory_list:
            if item == my_item:
                friends_vendor.add(my_item)
                self.remove(my_item)
                swap_happened = True
        for item in friends_vendor.inventory:
            if item == their_item:
                self.add(their_item)
                friends_vendor.remove(their_item)
                swap_happened = True
                
        # print([item.category for item in inventory_list])
        # print([item.category for item in friends_vendor.inventory])
        return swap_happened

    def swap_first_item(self, friend_vendor):
        if len(self.inventory) <= 0 or len(friend_vendor.inventory) <= 0:
            return False

        friends_first_item = friend_vendor.inventory[0]
        my_first_item = self.inventory[0]
        friend_vendor.inventory[0] = my_first_item
        self.inventory[0] = friends_first_item

        return True

    def get_best_by_category(self, category: str):
        category_list = self.get_by_category(category)
        if not category_list:
            return None
        highest_condition = 0
        best_item = category_list[0]
        for item in category_list:
            if item.condition > highest_condition:
                highest_condition = item.condition
                best_item = item
        return best_item    
    
# AISHA        
#     def get_best_by_category(self, category):
#         get_category = self.get_by_category(category)
#         if not get_category:
#             return None
#         best_condition = 0
#         best_item = get_category[0]
#         for item in get_category:
#             if item.condition > best_condition:
#                 best_condition = item.condition
#                 best_item = item
#         return best_item

# # Method 2:
#     def get_best_by_category(self, category):
#         get_category = self.get_by_category(category)
#         if not get_category:
#             return None
#         for item in get_category:
#             return max(get_category, key = lambda item : item.condition)
