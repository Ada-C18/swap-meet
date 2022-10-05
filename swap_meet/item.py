
class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition    

    def __str__(self):
        return "Hello World!"


    def condition_description(self):
        if not self.condition:
            return False
        elif self.condition <= 1:
            return "Heavily Used"
        elif self.condition <= 2:
            return "Fair condition"
        elif self.condition <= 3:
            return "Good condition"
        elif self.condition <= 4:
            return "Normal condition"
        else:
            return "Excellent condition"


