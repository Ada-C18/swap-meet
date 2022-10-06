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
        # get_category = self.get_by_category(category)
        # best_item = None
        # # loop through get_category
        # if best_item in get_category:
        #     return max(get_category(best_item))

    def get_best_by_category(self,category):
        get_category = self.get_by_category(category)
        best_item = None

        for item in get_category:
            if item not in get_category or get_category == None:
                return best_item


        if get_category:  # IF its true and category is in get_category
            
            #CREATE LAMBDA DICT WITH ITEM: ITEM.CONDITION
            #NOW ASSIGN IT TO BEST ITEM
            #BEST ITEM IS NOW CALLING THE MAX FOR THE VAR GET_CATEGORY
            best_item = max(get_category, key = lambda item: item.condition)
            print(best_item)
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        #other = other_vendor to trade with
        #my_p = a cat self.vend wants
        #their_p = a cat tha other.vender wants
        
        best_item_i_want = self.get_best_by_category(their_priority)
        their_best_item_i_want = other_vendor.get_best_by_category(my_priority)
        if not best_item_i_want or best_item_i_want:
            return False
        else:
            return self.swap_items(other_vendor, best_item_i_want,their_best_item_i_want)
    # # refactoring - look at get_by_category to update this function
    #     best_item_dictionary = {}

    #     # building dictionarty with categories as keys and values as None
    #     for category in self.get_by_category:
    #         if category not in best_item_dictionary:
    #             best_item_dictionary[category] = None
        
    #     #looping through the inventory to get each item
    #     for item in self.inventory:
    #         # for each item, create dictionary entry based on category
    #         best_item_dictionary[category] = [item]
    #         # if the category already exists in the dictionary, add item
    #         # to value list
            
    #         if item > best_item_dictionary and best_item == category:
    #             return item


            # best_item = self.inventory[0]