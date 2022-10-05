class Vendor:
    def __init__(self,inventory = None):
        if inventory is None:
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
        else:
            return False
    def get_by_category(self,category):
        list_category= []
        for item in self.inventory:
            if  item.category == category:
                list_category.append(item) 
        return list_category

    def swap_items(self,vendor,my_item,their_item):

        if their_item in vendor.inventory and my_item in self.inventory:
        
            vendor.remove(their_item)
            self.add(their_item)

            self.remove(my_item)
            vendor.add(my_item)
            return True
        else:
            return False

    def swap_first_item(self,vendor):
        if len(self.inventory) != 0 and len(vendor.inventory)!= 0 :
            temp_holding_item = self.inventory[0]
            self.inventory[0] = vendor.inventory[0]
            vendor.inventory[0] = temp_holding_item
            return True
        else:
            return False

        

