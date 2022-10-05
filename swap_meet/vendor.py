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

    def swap_first_item(self, friends_vendor):
        swap_first_element = False
        if len(self.inventory) > 1 and len(friends_vendor.inventory) > 1:
            temp = self.inventory[0]
            self.inventory[0] = friends_vendor.inventory[0]
            friends_vendor.inventory[0] = temp
            swap_first_element = True            
        
        else:
            swap_first_element = False
            
        return swap_first_element
        
