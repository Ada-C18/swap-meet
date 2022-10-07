class Item:
    def __init__(self, category = '', condition = 0, age = 0):
        self.category = category
        self.condition = condition
        self.age = age


    def __str__(self):
        return f"Hello World!"

    def condition_description(self):
        
        description = {
            0: 'bad',
            1: 'poor',
            2: 'decent',
            3: 'average',
            4: 'good',
            5: 'pristine'
        }
        
        condition = int(self.condition)

        for rating, quality in description.items():
            if condition == rating:
                return quality 
        
