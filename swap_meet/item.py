class Item:
    
    def __init__(self, category= "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return ("Hello World!")


    # conditional statements 
    
    def condition_description(self):

        if self.condition == 5:
            description = "Perfect"
        elif 0 <= self.condition <= 2:
            description = "Used with minor flaws"
        elif 2.1 <= self.condition <= 3:
            description = "Used with little to no flaws"
        elif 3.1 <= self.condition <= 4.9:
            description = "Like New"
        return description
        
    
    #    condition_dict = {
    #         "0": "Used with visible flaws",
    #         "1": "Used with minor flaws",
    #         "2": "Used with little to no flaws",
    #         "3": "Used with no flaws",
    #         "4": "Like new",
    #         "5": "Perfect condition"
    #     }
    #     return(condition_dict[condition_rate])

    

