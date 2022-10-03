class Vendor:
    def __init__(self,inventory=[]):
        self.inventory=inventory

    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    def get_by_category(self,description):
        category_list=[]
        for item in self.inventory:
            if item.category==description:
                category_list.append(item)
        return category_list

    def swap_items(self,other_vendor,my_item,their_item):
        other_vendor.add(self.remove(my_item))
        self.add(other_vendor.remove(their_item))
        return self.remove(my_item) and other_vendor.remove(their_item)
        