class Vendor:
    def __init__(self, inventory = []):
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

vendor = Vendor()
inventory = ["a", "b", "c"]
vendor = Vendor(inventory)












    # def swap_items(self,vendor_2 my_item, their_item):
    #     if my_item in self.inventory and their_item in vendor_2.inventory





    

 
    

    
