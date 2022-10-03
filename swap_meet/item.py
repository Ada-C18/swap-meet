class Item:
    def __init__(self,category = "",condition = 0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return 'Hello World!'
    
    def condition_description(self):
        descriptions = {
            0: "Either no rating or it is really not useable",
            1: "would not recommend",
            2: "hopefully it is a good deal",
            3: "what you would expect",
            4: "pretty good",
            5: "NWT"
            }
        
        for rating,description in descriptions.items():
            if self.condition == rating:
                return description 