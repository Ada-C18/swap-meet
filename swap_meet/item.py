DESCRIPTION_DICT = {
    0: "Did you even check?",
    1: "Possibly good for parts, possibly.",
    2: "A good holiday gift for your least favorite relative. ",
    3: "Not bad...",
    4: "Worth the price of admission.",
    5: "A hidden treasure for Antiques Roadshow.",
}


class Item:

    # TODO: maybe we should reorder these arguments if category is 
    # set by default in child classes?
    def __init__(self, category = "", condition=0):
        """
        sets up the Item instance with an optional category attribute
        """
        
        self.category = category
        self.condition = condition 

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        """
        Return a string description based on self.condition.
        """

        if self.condition < 0 or self.condition > 5:
            return "Did you even read the instructions?"
            
        rounded_score = round(self.condition)
        return DESCRIPTION_DICT[rounded_score]


