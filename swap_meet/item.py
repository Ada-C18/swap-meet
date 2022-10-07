class Item:
    def __init__(self, category = '', condition = 0, age = 0):
        self.category = category
        self.condition = condition
        self.age = age


    def __str__(self):
        return f"Hello World!"

    def condition_description(self):
        condition = int(self.condition)
        if condition == 0:
            return 'bad'
        if condition == 1:
            return 'poor'
        if condition == 2:
            return 'decent'
        if condition == 3:
            return 'average'
        if condition == 4:
            return 'good'
        if condition == 5:
            return 'pristine'
        
