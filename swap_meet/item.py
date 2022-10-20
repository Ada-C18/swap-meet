class Item:

    category = ""
    
    
    def __init__(self, category=category, condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return ("Hello World!")
    
    def condition_description(self, condition_rate):
        condition_dict = {
            "0": "Used with visible flaws",
            "1": "Used with minor flaws",
            "2": "Used with little to no flaws",
            "3": "Used with no flaws",
            "4": "Like new",
            "5": "Perfect condition"
        }
        return(condition_dict[condition_rate])

    

