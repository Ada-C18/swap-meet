class Item:
    def __init__(self, category = "", condition = 0.0):
        self.category = category
        self.condition = condition

        
    def __str__(self):
        self.item = "Hello World!"
        return self.item

    def condition_description(self):
        if 0 < self.condition < 1:
            self.condition = "should be free tbh"
            return self.condition 
        elif 1 < self.condition < 2:
            self.condition = "heavily used"
            return self.condition 
        elif 2 < self.condition < 3:
            self.condition = "slightly used"
            return self.condition 
        elif 3 < self.condition < 4:
            self.condition = "good condition"
            return self.condition 
        elif 4 < self.condition <= 5:
            self.condition = "new with tags"
            return self.condition 




    