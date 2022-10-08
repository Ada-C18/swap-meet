
import math


class Item:
    def __init__(self, category="", condition=0.0, age=0):
        if not isinstance(category, str) or not isinstance(condition, (float, int)) or not isinstance(age, (float, int)):
            raise TypeError(
                "Invalid parameters. Please check category is string, condition is float and age is float")
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):

        # We need to round DOWN floats in order to pass test_wave_05: test 5, which YES, we altereed to test a theory Isabella had. If a float is used on the object that the assertion is testing, it will fail if rounded up from .6
        if self.condition < 0:
            self.condition = abs(self.condition)
        self.condition = int(self.condition + .5)
        if self.condition > 5:
            self.condition = 5
        condition_dict = {
            0: "poor",
            1: "mhaa",
            2: "hmmm",
            3: "okay",
            4: "YeahAaaa.",
            5: "GIMME!!!"
        }
       
        return condition_dict[self.condition]

    # alternate implementation:
    #
    # def condition_description(self):
    #     if self.condition > 5:
    #         return "wow"
    #     elif self.condition > 4:
    #         return "ooo"
    #     elif self.condition > 3:
    #         return "okay"
    #     elif self.condition > 2:
    #         return "eh"
    #     else:
    #         return "meh"
