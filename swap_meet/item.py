from distutils.archive_util import make_archive
from operator import itemgetter
import py_compile

class Item:
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__ (self):
        return "Hello World!"

    def condition_description(self, poor=0, fair=1, good=2, excellent=3, perfect=4, new=5):
        self.poor = float(poor)
        self.fair = float(fair)
        self.good = float(good)
        self.excellent = float(excellent)
        self.perfect = float(perfect)
        self.new = float(new)