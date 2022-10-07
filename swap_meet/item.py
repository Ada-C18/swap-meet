class Item:
    def __init__(self, age = 0, category = "", condition = 0):
        self.category = category
        self.condition = condition
        self.age = age
        
# Wave 3       
    def __str__(self):
        return "Hello World!"

# Wave 5
    def condition_description(self):
        condition_descriptions = ["I dont like zero", "I dont like one either", 
        "Maybe I like two", "Hmmmm.....probably three is nice", "I like four",
        "Five is a nice number"]
        return condition_descriptions[self.condition]

        


    
        
