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

        if self.condition == 0:
            return "Bad"
        elif self.condition == 1:
            return "Almost bad"
        elif self.condition == 2:
            return "Meh"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 4:
            return "Great"
        elif self.condition == 5:
            return "Nothing is perfect, but it almost is"
