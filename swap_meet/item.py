from distutils.archive_util import make_archive
from operator import itemgetter
import py_compile

class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__ (self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "poor"
        elif self.condition == 1:
            return "fair"
        elif self.condition == 2:
            return "good"
        elif self.condition == 3:
            return "excellent"
        elif self.condition == 4:
            return "perfect"
        elif self.condition == 5:
            return "new"