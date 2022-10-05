class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        '''
        Method to stringify/convert an instance of Item to a str
        '''
        return "Hello World!"

    def condition_description(self):
        # handle condition if it's a float
        if type(self.condition) == float:
            self.condition = int(self.condition)

        if self.condition == 0.0:
            return "Bad"
        elif self.condition == 1.0:
            return "Almost bad"
        elif self.condition == 2.0:
            return "Meh"
        elif self.condition == 3.0:
            return "Good"
        elif self.condition == 4.0:
            return "Great"
        elif self.condition == 5.0:
            return "Nothing is perfect, but it almost is"
