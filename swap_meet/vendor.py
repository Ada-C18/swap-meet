from operator import truediv
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = list()) -> None:
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item) -> bool:
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False