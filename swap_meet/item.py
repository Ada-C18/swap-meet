from distutils.archive_util import make_archive
from operator import itemgetter
import py_compile

class Item:
    def __init__(self, category=""):
        self.category = category

    def __str__ (self):
        return "Hello World!"