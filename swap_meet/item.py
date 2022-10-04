# from swap_meet.vendor import Vendor
class Item:
<<<<<<< HEAD
    def __init__(self, category=None):
        self.category = category if category is not None else ""


=======
    def __init__(self, category=""):
        self.category = category

    # __str__ is called when str() function is invoked on an object
    def __str__(self):
        return "Hello World!"
>>>>>>> c0ce8dd9224ee149f1261892deff50b4ba2f44d8
