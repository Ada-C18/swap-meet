from swap_meet.item import Item
class Vendor(Item):
    def __init__(self, inventory=[]):
        super().__init__(category='')
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
    
    #Wave 3
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
    
    #Wave 4
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
            
        


            