class Item:
    def __init__(self, category='', condition=0, age=0):
        self.category = category
        self.condition = condition
        self.age = age
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        conditions = {
            0: "poo",
            1: "meh",
            2: "serviceable",
            3: "decent",
            4: "waow",
            5: "bomb"
        }
        return conditions[self.condition]