from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory

        if self.inventory is None:
            self.inventory = []
    
    def add(self, item):
        self.item = item
        self.inventory.append(item)
        return self.item

    def remove(self, item):
        self.item = item
        if self.item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
        return self.item

    
    def get_by_category(self, category):
        # return [item for item in self.inventory if item.category == category]
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list

    def swap_items(self, friend, my_item, their_item):
        self.friend = friend
        self.my_item = my_item
        self.their_item = their_item
        
        if self.their_item not in friend.inventory or self.my_item not in self.inventory:
            return False

        if self.my_item:
            friend.inventory.append(my_item)
            self.inventory.remove(my_item)
        
        if self.their_item:
            self.inventory.append(their_item)
            friend.inventory.remove(their_item)
            return True
        
    def swap_first_item(self, friend):
        self.friend = friend
        
        if len(friend.inventory)==0 or len(self.inventory)==0 :
            return False
        
        self_item = self.inventory.pop(0)
        friend.inventory.append(self_item)

        friend_item= friend.inventory.pop(0)
        self.inventory.append(friend_item)
        
        return True

    
    def get_best_by_category(self, category):
        get_category = self.get_by_category(category)
        if not get_category:
            return None
        best_condition = 0 
        best_item = get_category[0]
        for item in get_category:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item

       
       
       
       
       
       
       
       
       
       
       
       
        # item_list = []
        # if category not in self.inventory:
        #     return None
        # for item in self.inventory:
        #     if item.category == category:
        #         item_list.append(item)

        # return max(item_list, key = item.condition)
    # def get_condition(inventory):
    #     return self.condition
    
    # def get_best_by_category(self, category):
    #     get_category = self.get_by_category(category)
    #     if not get_category:
    #         return None
    #     print(str(get_category))
    #     for item in get_category:
    #         return max(item, key = item.condition)
    
    # def get_condition(self):
    #     for item in self.inventory:
    #         return int(item.condition)


    