class Item:
    def __init__(self, category=None, condition=None):
        self.category = category if category is not None else ""
        self.condition = condition if condition is not None else 0
    
    def __str__(self):
        return "Hello World!"
    
def condition_description(self):
        description_options = ['Poor','Used fair','Used good','Used very good','Used like new', 'New']
        return description_options[self.condition]
