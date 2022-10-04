class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []

    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return False
        self.inventory.remove(item_to_remove) #is remove the best method here? only deletes first instance of item_to_remove in list
        return item_to_remove
    
    def get_by_category(self, category):
        # items_in_category = [] #this will be a list of instances of Item 
        # for item in self.inventory:
        #     if item.category == category:
        #         items_in_category.append(item)
        
        # return items_in_category

        #list comprehension
        items_in_category = [item for item in self.inventory if item.category == category]
        return items_in_category 

    def swap_items(self, other_vendor, my_item, their_item):
        #guard clause in the event that item to swap is not available 
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        #if items to swap are available, add items to new list and remove items from old lists
        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)
        other_vendor.inventory.append(my_item)
        self.inventory.remove(my_item)
        return True

    def swap_first_item(self, other_vendor): 
        if not self.inventory or not other_vendor.inventory:
            return False
        self.inventory.append(other_vendor.inventory[0])
        other_vendor.inventory.pop(0)
        other_vendor.inventory.append(self.inventory[0])
        self.inventory.pop(0)
        return True