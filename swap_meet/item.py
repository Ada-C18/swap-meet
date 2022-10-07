
class Item:
    """
    A class to represent an item. 
    """
    
    def __init__(self, category = "", condition = 0):
        """
        Constructs attributes for the item object:
        category name and condition of the item.
        """
        self.category = category
        self.condition = condition    

    
    def __str__(self):
        """
        Prints the string "Hello World".
        """
        return "Hello World!"

    
    
    def condition_description(self):
        """
        Return the condition describtion of the item.
        """
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

    


