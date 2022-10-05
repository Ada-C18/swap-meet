from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
        
        

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
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items

    def swap_items(self, another_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in another_vendor.inventory:
            return False
        else:
            self.remove(my_item) 
            another_vendor.add(my_item)
            another_vendor.remove(their_item)
            self.add(their_item)
            return True


    def swap_first_item(self, another_vendor):
        if self.inventory == [] or another_vendor.inventory == []:
            return False
        else:
            my_first_item = self.inventory[0]
            their_first_item = another_vendor.inventory[0]
            return self.swap_items(another_vendor, my_first_item, their_first_item)
            



   
            
   
            
            

vendor = Vendor()

vendor = Vendor(inventory =["a", "b", "c"])





item = Item()
item_a=Item("clothing")
item_b =Item("electronics")
item_c = Item("clothing")
vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )




my_item = item_a = Item(category="clothing")
my_item = item_b = Item(category="clothing")
my_item =item_c = Item(category="clothing")
fatimah = Vendor(
    inventory=[item_a, item_b, item_c]
    )

their_item = item_d = Item(category="electronics")
their_item =item_e = Item(category="decor")
jolie = Vendor(
        inventory=[item_d, item_e]
    )


 






    

 
    

    
