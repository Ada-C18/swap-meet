import math


class Item:
    def __init__(self, category = "", condition = 0.0):
        self.category = category
        self.condition = condition

    def get_category(self):
        return self.category
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        description_word = [
            "bad condition",
            "poor condition",
            "acceptable condition",
            "fair condition",
            "good condition",
            "excellent condition"
            ]
        return description_word[math.floor(self.condition)]

          # description_word = ""
        # if self.condition == 0:
        #     description_word = "bad condition"
        # elif  0 < self.condition <= 1:
        #     description_word = "poor condition"
        # elif  1 < self.condition <= 2:
        #     description_word = "acceptable condition"
        # elif  2 < self.condition <= 3:
        #     description_word = "fair condition"
        # elif  3 < self.condition <= 4:
        #     description_word = "good condition"
        # else:
        #     description_word = "excellent condition"
        # return description_word
