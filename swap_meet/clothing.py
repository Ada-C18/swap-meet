from swap_meet.item import Item

# class Clothing(Item):
#     def __init__(self, condition = None):
        
#         super().__init__(condition, category = "Clothing") # default arg has to be at the end
            
#     def __str__(self): 
#         # print([cloth.category for cloth in self.inventory])
#         return 'The finest clothing you could wear.'
    
class Clothing(Item):
    def __init__(self):
        
        super().__init__(category = "Clothing")
        
    def __str__(self): 
        # print([cloth.category for cloth in self.inventory])
        return 'The finest clothing you could wear.'