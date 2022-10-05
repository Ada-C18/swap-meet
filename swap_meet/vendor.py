from types import MemberDescriptorType

#from swap_meet.item import Item

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


 

   
   
    
    




























    #takes in an instance of another vendor, representing friend they are swapping with
    def swap_first_item(self, Vendor): #
    
        if not self.inventory:
            return False
        
        # if not Vendor.inventory:
        #     return False
        
      #loop through items, remove item 0, append it to friends list 
      #self.inventory.remove()
      #self.inventory.add()

      #loop for appending items?
        for item in self.inventory:
            #self.inventory.remove(0)
            self.inventory.pop(0)
            Vendor.inventory.append(0)
     # loop through friend inventory, remove item 0, append to self inventory list      
    
    # short hand way to do it --  Vendor.inventory.append(self.inventory.pop(0))

            
    


