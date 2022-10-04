class Vendor:
    def __init__(self,inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    def get_by_category(self,category):
        list_category= []
        for item in self.inventory:
            if  item.category == category:
                list_category.append(item) 
        return list_category