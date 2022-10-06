from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
        # self.item = Item(self.category, self.condition)
        #am I able to use this as a composite of Item
        
        

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



    def get_best_by_category(self, category):
        
        items_in_category = self.get_by_category(category)

        if items_in_category == False:
            return None
        else: 
            best_item_so_far = None
            for item in items_in_category: 
                if best_item_so_far is None or best_item_so_far.condition < item.condition: 
                    best_item_so_far = item
            return best_item_so_far


    def swap_best_by_category(self, other, my_priority, their_priority):
        # my_priority="Clothing" #vendor wants to receive 
        # their_priority="Decor"#other wants to receive
       
        my_best_item_in_category =self.get_best_by_category(category =  their_priority)
        their_best_item_in_category = other.get_best_by_category(category = my_priority)
        if my_best_item_in_category == None or their_best_item_in_category == None:
            return False
        return self.swap_items(other,my_best_item_in_category,their_best_item_in_category)
        




item_a = Decor(condition=2.0)
item_b = Electronics(condition=4.0)
item_c = Decor(condition=4.0)
tai = Vendor(
    inventory=[item_a, item_b, item_c]
)

    # them
item_d = Clothing(condition=2.0)
item_e = Decor(condition=4.0)
item_f = Clothing(condition=4.0)
other =jesse = Vendor(
    inventory=[item_d, item_e, item_f]
)





# #me
# item_a = Decor(condition=2.0)
# item_b = Electronics(condition=4.0)
# item_c = Decor(condition=4.0)
# tai = Vendor(
#     inventory=[item_a, item_b, item_c]
# )

# #them
# item_d = Clothing(condition=2.0)
# item_e = Decor(condition=4.0)
# item_f = Clothing(condition=4.0)
# other =jesse = Vendor(
#     inventory=[item_d, item_e, item_f]
# )
        
        
#instance vendor no inventory
tai = Vendor(
        inventory=[]
    )

item_a = Clothing(condition=2.0)
item_b = Decor(condition=4.0)
item_c = Clothing(condition=4.0)
other = jesse = Vendor(
    inventory=[item_a, item_b, item_c]
)

#instance other no inventory            
item_a = Clothing(condition=2.0)
item_b = Decor(condition=4.0)
item_c = Clothing(condition=4.0)
tai = Vendor(
    inventory=[item_a, item_b, item_c]
)


other =jesse = Vendor(
    inventory=[]
)


   
            
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


 
item_a = Clothing(condition=2.0)
item_b = Decor(condition=2.0)
item_c = Clothing(condition=4.0)
item_d = Decor(condition=5.0)
item_e = Clothing(condition=3.0)
tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )




    

 
    

    
