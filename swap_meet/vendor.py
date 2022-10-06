# from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory=[]):
        self.inventory = inventory
        if not inventory:
            self.inventory = [] 

    def add(self, item):
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
    
    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item not in self.inventory or \
            their_item not in friend_vendor.inventory:
            return False
        item_to_give = self.remove(my_item)
        friend_vendor.add(item_to_give)
        item_to_get = friend_vendor.remove(their_item)
        self.add(item_to_get)
        return True

    def swap_first_item(self, friend_vendor):
        if not self.inventory or not friend_vendor.inventory:
            return False
        my_first_item = self.inventory[0]
        friend_first_item = friend_vendor.inventory[0]
        self.remove(my_first_item)
        friend_vendor.add(my_first_item)
        friend_vendor.remove(friend_first_item)
        self.add(friend_first_item)
        return True

    # def get_best_by_category(self, category):
    #     # get_category = self.get_by_category(category)
    #     # best_item = None
    #     # # loop through get_category
    #     # if best_item in get_category:
    #     #     return max(get_category(best_item))
    #     # category_list = self.get_by_category
    #     best_item_dictionary = {}
    #     # building dictionary with categories as keys and values as None
    #     for item in self.inventory:
    #         if item.category not in best_item_dictionary:
    #             best_item_dictionary[item.category] = item.condition
    #         else:
    #             if item.condition > best_item_dictionary[item.category]:
    #                 best_item_dictionary[item.category] = item.condition
    #     # print(best_item_dictionary)
    #     if category not in best_item_dictionary.keys():
    #         return None
    #     for key, value in best_item_dictionary.items():
    #         if key == category:
    #             print(key, value)
    #             return f"{key} {value}"
    #             # return item.category
        
    #     #looping through the inventory to get each item
    #     # for item in self.inventory:
    #     #     if item.condition > best_item_dictionary[category]:
    #     #         best_item_dictionary[category] = item
    #     # return best_item_dictionary

    def get_best_by_category(self,category):
        get_category = self.get_by_category(category)
        best_item = None

        if not get_category:
            return best_item

        if get_category: 
            best_item = max(get_category, key = lambda item: item.condition)

        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):

        best_item_they_want = self.get_best_by_category(their_priority)
        their_best_item_i_want = other.get_best_by_category(my_priority)
        if not best_item_they_want or not their_best_item_i_want:
            return False
        else:
            return self.swap_items(other, best_item_they_want,their_best_item_i_want)
            
    