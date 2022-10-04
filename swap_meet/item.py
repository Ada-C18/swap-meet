'''
module: item.py
    class: Item
        attribute: .inventory
        method: .add .remove
'''

class Item:

    def __init__(self, category = None):
        if category: # not empty:
            self.category = category
        else: 
            self.category = "" # default