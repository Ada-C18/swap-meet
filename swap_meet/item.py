class Item:
    def __init__(self, category="", condition=0):
        if category is None:
            self.category = ""
        self.category = category
        self.condition = condition

    def __str__(self):
       return "Hello World!"

    def condition_description(self):
        # is there a more concise way? for loop?
        if self.condition == 0:
            zero_condition_description = "Yo, this is bad. Reconsider."
            return zero_condition_description
        elif self.condition == 1:
            one_condition_description = "You could probably find better... but this'll do."
            return one_condition_description
        elif self.condition == 2:
            two_condition_description = "If you're okay with some dings and things."
            return two_condition_description
        elif self.condition == 3:
            three_condition_description = "Lots of life left in this one."
            return three_condition_description
        elif self.condition == 4:
            four_condition_description = "Oooh, quite the find! Barely a scratch."
            return four_condition_description
        elif self.condition == 5:
            five_condition_description = "ULTRA RARE, PERFECT CONDITION."
            return five_condition_description