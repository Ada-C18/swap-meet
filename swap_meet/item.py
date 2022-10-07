class Item:
    def __init__(self, category = "", condition=0.0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        self.item = "Hello World!"
        return self.item

    def condition_description(self):
        {}
        if 0 < self.condition <= 1:
            return "should be free tbh"

        elif 1 < self.condition <= 2:
            return "heavily used"

        elif 2 < self.condition <= 3:
            return "slightly used"

        elif 3 < self.condition <= 4:
            return "good condition"

        elif 4 < self.condition <= 5:
            return "new"





    