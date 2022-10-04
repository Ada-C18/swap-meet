from swap_meet.item import Item
class Vendor(Item):
    def __init__(self, inventory=[]):
        super().__init__(category='')
        self.inventory = inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        for check_item in self.inventory:
            if check_item == item:
                self.inventory.remove(item)
                return item
        return False
      
    def get_by_category(self, category):
        result = []
        for each_item in self.inventory:
            if each_item.category == category:
                result.append(each_item)
        return result
    
        
        
      
      