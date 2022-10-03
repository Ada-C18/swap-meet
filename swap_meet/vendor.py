from pickle import FALSE

class Vendor:
    def __init__(self,inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return FALSE
    
    def get_by_category(self,category):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items
    
    def swap_items(self,other_vendor,my_item,their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.append(other_vendor.inventory.pop(other_vendor.inventory.index(their_item)))
            other_vendor.inventory.append(self.inventory.pop(self.inventory.index(my_item)))
            return True
        return False

    
    def swap_first_item(self,other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            self.inventory.insert(0,other_vendor.inventory.pop(0))
            other_vendor.inventory.insert(0,self.inventory.pop(1))
            return True

    def get_best_by_category(self,category):
        condition = -1
        highest_condition_item = ""
        if self.inventory:
            category_included = False
            for item in self.inventory:
                if item.category == category:
                    category_included = True
            if category_included == True:
                for item in self.inventory:
                    if item.condition > condition  and item.category == category:
                        highest_condition_item = item
                        condition = item.condition
                return highest_condition_item
    
    def swap_best_by_category(self,other,my_priority,their_priority):
        if self.get_best_by_category(their_priority) and other.get_best_by_category(my_priority):
            self.swap_items(other,self.get_best_by_category(their_priority),other.get_best_by_category(my_priority))
            return True
        else:
            return False
    
    def get_newest(self):
        age = 10000000000000
        newest_item = ""
        for item in self.inventory:
            if item.age < age:
                newest_item = item
                age = item.age
        return newest_item
    
    def swap_by_newest(self,other):
        self.swap_items(other,self.get_newest,other.get_newest)
        
    