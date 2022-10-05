class Item:
    def __init__(self, age=None, category = "", condition=0):
        """
        Input: requires age, and takes in a category and condition
        as parameters.
        Result: defines attributes category and condition
        """
        self.age = age
        self.category = category
        self.condition = condition
    
    def __str__(self):
        """
        When stringifying an Item using str(), turns it into "Hello World!"
        """
        return "Hello World!"

    def condition_description(self):
        """
        Input: an instance with a value for an attribute condition
        Output: returns a description based on the condition value
        """

        if self.condition == 5:
            return "Absolutely perfect! I love that for you (^‿◕)"
        elif self.condition > 4:
            return "Almost absolutely perfect! Aren't you lucky ☘☘☘"
        elif self.condition > 3:
            return "Not too shabby!"
        elif self.condition > 2:
            return "They're a little fixer upper"
        elif self.condition > 1:
            return "Be gentle with this one, it's a bit (or very) used"
        else:
            return "Do an exorcism first...just in case"
