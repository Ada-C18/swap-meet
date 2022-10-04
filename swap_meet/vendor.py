class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory

        if inventory is None: #if inventory is None(empty)
            self.inventory = []
            
    def add(self, item): #instance called add thats add item to the inventory empty list
        self.inventory.append(item)
        return item

    def remove(self, item): #instance removes the matching item from the inventory and return item that was removed
        if item in self.inventory: # if item is inventory remove item
            self.inventory.remove(item)
            return item
        else: #if is no matching item in the inventory return False
            return False

    def get_by_category(self, category):#instance get_by_category takes one argument(string) representing a category, returns a list of items in the invetory with that category
        category_list = []
        for item in self.inventory:
            if item.category == category: #if item is the category
                category_list.append(item) #append item in the category
        return category_list #return category
    
    def swap_items(self, vendor, my_item, their_item):# swap items between my_item, their_item
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.append(their_item)#append their_item in inventory
            vendor.inventory.append(my_item)#append my_item in vendor inventory
            self.inventory.remove(my_item)#remove my_item from inventory
            vendor.inventory.remove(their_item)#remove their_item from vendor inventory
            return True
        else: #if vendor's inventory doen't contain my_item or the friend's inventory doesn't contain their_item returns False
            return False

    def swap_first_item(self, vendor):#swap first item in the instance's(self)inventory and the first item in the friend's(vendor) inventory
        if self.inventory and vendor.inventory:
            my_item = self.inventory[0]# my_item = first item in the instance's(self)inventory
            their_item = vendor.inventory[0]#their_item = first item in the friend's(vendor) inventory
            self.inventory.append(their_item)#append instance(self) inventory in their_item
            vendor.inventory.append(my_item)#append my_item in the vendor inventory
            self.inventory.remove(my_item) # remove my_item from instance(self) inventory
            vendor.inventory.remove(their_item)#remove their_item from vendor inventory
            return True
        else:#if either itself or the friend have an empty inventory, the method returns False
            return False
 

