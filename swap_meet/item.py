class Item:
    def __init__(self, category = "", condition=0):
        self.category = category 
        self.condition = condition 
    

    def __str__(self):
        return "Hello World!"
    

    def condition_description(self):
        rating = self.condition 
        description = ["very gross", "Not that great", "It's okay...", "gently used", "pretty good", "really great!"]
        return description[rating]
