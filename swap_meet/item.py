class Item:
    def __init__(self, category= "", condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        match self.condition:
            case 0:
                return 'Falling apart'
            case 1:
                return 'Very used'
            case 2:
                return 'Used'
            case 3:
                return 'Slightly used'
            case 4:
                return 'Open but unused'
            case 5:
                return 'Brand New'