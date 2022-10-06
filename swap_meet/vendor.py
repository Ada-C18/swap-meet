from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = None):

        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):                         
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        return [item for item in self.inventory if category == item.category]
        # items_list = []
        # for item in self.inventory:
        #     if category == item.category:
        #         items_list.append(item)
        # return items_list

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        
        self.add(their_item)
        friend.add(my_item)
        self.remove(my_item)
        friend.remove(their_item)

        return True

    #Takes in an instance of another vendor and trades first item from self and vendor list
    def swap_first_item(self, friend):

    #return false if either list does not have item
        if not self.inventory or not friend.inventory:
            return False

        self.swap_items(friend, self.inventory[0], friend.inventory[0])
        return True

        
#wave 6
# Get the item with the best condition in a certain category
    def get_best_by_category(self, category):
        #assign variable best_category to get_by_category above to invoke
        best_category = self.get_by_category(category)

        # If there are no items in the `inventory` that match the category return `None
        if not best_category:
            return None 

        #variable to compare
        best_condition = best_category[0]

        # Loop through the instance's `inventory` for the item with the highest condition and associated category
        for item in best_category:
            if item.condition > best_condition.condition:
                best_condition = item

        # Return item
        return best_condition 

    def swap_best_by_category(self,other, my_priority, their_priority):
        #access best category for each parameter
        self_best_category = self.get_best_by_category(their_priority)

        their_best_category = other.get_best_by_category(my_priority)

        #if there are not matches or empty return false
        if not self_best_category or not their_best_category:
            return False
    
        self.swap_items(other, self_best_category, their_best_category)

        return True