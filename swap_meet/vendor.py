from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False

        self.inventory.remove(item) #is .remove the real thing to use?
        
        return item

    def get_by_category(self, a_category):
        self.a_category: a_category
        items = []
        for item in self.inventory:
            if item.category == a_category:
                items.append(item)
        return items
    
    def swap_items(self, friend, my_item, their_item):
        self.friend = friend
        self.my_item = my_item
        self.their_item = their_item
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        else:    
            self.remove(my_item)
            friend.add(my_item)
            
            friend.remove(their_item)
            self.add(their_item)
            return True

    def swap_first_item(self, friend):
        self.friend = friend

        if len(self.inventory) != 0 and len(friend.inventory) != 0:
            self.add(friend.inventory[0])
            friend.add(self.inventory[0])

            self.remove(self.inventory[0])
            friend.remove(friend.inventory[0])
            
            return True
    
    def get_best_by_category(self, category):
#COULD COME BACK AND TRY USING A MAX FXN AND LAMDA EXPRESSION
#If there are no items in the inventory that match the category, it returns None

        # instance = self.get_by_category(category)
        # attribute = instance.a_category
        best_condition = None
        best_condition_val = 0

#Loop through the items of the correct category
        for item in self.get_by_category(category):
#If the condition of the item is more than the current best condition of all items
            if item.condition > best_condition_val:
#Update the best_condition_val with the current highest condition
                best_condition_val = item.condition
#append the value of best_condition with the item with the current highest condition
                best_condition = item 
        # if best_condition == "":
            # return None
        return best_condition


    def swap_best_by_category():
        pass