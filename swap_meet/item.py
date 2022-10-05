class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition < 1:
            return "Unusable"
        if 1 <= self.condition < 2:
            return "Bad" 
        if 2 <= self.condition < 3: 
            return "Okay"
        if 3 <= self.condition < 4:
            return "Good"
        if 4 <= self.condition < 5: 
            return "Great"
        if self.condition >= 5:
            return "Perfect"

        # Jennifer had this solution but it is not supported with Python 3.9
        # match evaluates the expression and runs whichever case matches the value
        
        # match self.condition:
        #     case 0:
        #         return 'Falling apart'
        #     case 1:
        #         return 'Very used'
        #     case 2:
        #         return 'Used'
        #     case 3:
        #         return 'Slightly used'
        #     case 4:
        #         return 'Open but unused'
        #     case 5:
        #         return 'Brand new'
