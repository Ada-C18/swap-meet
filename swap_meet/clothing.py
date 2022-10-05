from swap_meet.item import Item

class Clothing(Item):

    def __init__(self,category="Clothing",condition=0) -> None:
        self.category=category
        self.condition=condition
        
        #self.condition_decription="hi"
    
    def __str__(self): 
        return "The finest clothing you could wear."
    
    #def condition_description(self):
        
        
        

        # class Pizza:
#     def __init__(self, toppings):
#         self.toppings = toppings
#     def calculate_toppings_price(self):
#         return 0.75 * len(self.toppings)
# class FancyPizza(Pizza):
#     def calculate_toppings_price(self):
#         return (2.50 * len(self.toppings)) + 5
