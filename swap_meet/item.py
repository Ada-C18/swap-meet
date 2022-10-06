# In Wave 2 we will create the Item class and the get_by_category method.
# There is a module (file) named item.py inside of the swap_meet package (folder)
# Inside this module, there is a class named Item
# Each Item will have an attribute named category, which is an empty string by default
# When we initialize an instance of Item, we can optionally pass in a string with the keyword argument category
# 
class Item:
    def __init__(self, category = None, condition = None, age=None):
        self.category = category if category is not None else ""
        self.condition = condition if condition is not None else 0
        self.age = age if age is not None else 0

    def __str__(self):
        return "Hello World!"
    def condition_description(self):
        condition = {
            0:"bad shape",
            1:"very used",
            2:"acceptable",
            3:"good condition",
            4:"great condition",
            5:"minted"}
        return condition[self.condition]