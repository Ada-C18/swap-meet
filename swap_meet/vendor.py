from swap_meet.item import Item
class Vendor(Item):
    def __init__(self, inventory = None):
        super().__init__(category='')
        if inventory is None:
            inventory = []
        self.inventory = inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        for check_item in self.inventory:
            if check_item == item:
                self.inventory.remove(item)
                return item
        return False
    # Wave 2 
    def get_by_category(self, category):
        result = []
        for each_item in self.inventory:
            if each_item.category == category:
                result.append(each_item)
        return result
    
    # Wave 3
    def swap_items(self, friend, my_item, their_item):
        my_swap = False
        friend_swap = False
        for i in self.inventory:
            if i == my_item:
                my_swap = True
        for fi in friend.inventory:
            if fi == their_item:
                friend_swap = True
        
        if my_swap == True and friend_swap == True:  
            self.remove(my_item)
            friend.add(my_item)
            friend.remove(their_item)
            self.add(their_item)     
            return self.inventory 
        return False
    
    # Wave 4
    def swap_first_item(self, friend):
        if self.inventory != [] and friend.inventory != []:
            my_swap = self.inventory[0]
            friend_swap = friend.inventory[0]
            self.remove(my_swap)
            friend.add(my_swap) 
            friend.remove(friend_swap)
            self.add(friend_swap)
            return self.inventory
        else:
            return False
    
    # Wave 6
    def get_best_by_category(self, category_str):
        best_rate = 0
        result = []
        for item in self.inventory:
            if item.category == category_str and best_rate < item.condition:
                best_rate = item.condition
                if result == []:
                    result.append(item)
                else:
                    result.pop()
                    result.append(item)
        if result == []:
            return None
        return result[0]
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_swap = other.get_best_by_category(my_priority)
        # print(my_swap.condition)
        other_swap = self.get_best_by_category(their_priority)
        # print(other_swap.condition)
        if other.inventory == [] or self.inventory == []:
            return False
        elif my_swap == None or other_swap == None:
            return False
        else:
            self.remove(other_swap)
            other.remove(my_swap)
            other.add(other_swap)
            self.add(my_swap)
            return True


            