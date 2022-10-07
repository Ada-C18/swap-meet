class Vendor:
    def __init__(self, inventory = None, condition = None):
        
        if inventory == None:
            self.inventory = []
        else: 
            self.inventory = inventory
        

    def add(self, added_item):
        self.inventory.append(added_item)
        return added_item

    def remove(self, removed_item):
        if removed_item not in self.inventory:
            return False
        self.inventory.remove(removed_item)
        return removed_item

    def get_by_category(self,category):
        items_in_category = []

        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
            
        return items_in_category


    def swap_items(self, another_vendor, my_item, their_item):
        if their_item not in another_vendor.inventory or my_item not in self.inventory:
            return False 
        self.remove(my_item)
        another_vendor.remove(their_item)
        another_vendor.add(my_item)
        self.add(their_item)
        return True 

    def swap_first_item(self, another_vendor):
        if another_vendor.inventory == [] or self.inventory == []:
            return False 

        another_item = another_vendor.inventory[0]
        my_item = self.inventory[0]

        self.swap_items(another_vendor, my_item, another_item)
        return True

    def get_best_by_category(self, category = ""):
        best_condition_rating = 0 
        best_condition_item = None
        if self.inventory == []:
            return False 
        for item in self.inventory:
            if item.category == category:
                if item.condition > best_condition_rating:
                    best_condition_rating  = item.condition
                    best_condition_item = item
        return best_condition_item
        

    def swap_best_by_category(self, another_vendor, my_priority, their_priority):
        
        best_item_found_for_other_vendor = self.get_best_by_category(their_priority)
        print(best_item_found_for_other_vendor)
        best_item_found_for_me = another_vendor.get_best_by_category(my_priority)
        print(best_item_found_for_me)
        


        if best_item_found_for_other_vendor is  None and best_item_found_for_me is not None:
            self.swap_items(another_vendor, best_item_found_for_me, best_item_found_for_other_vendor)
            print(self.swap_items(another_vendor, best_item_found_for_me, best_item_found_for_other_vendor))
            return True
        return False


            



    


        



    
