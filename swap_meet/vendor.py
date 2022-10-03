class Vendor:
    def __init__(self,inventory=None):
        if inventory==None:
            inventory=[]
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
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        given=self.remove(my_item)
        taken=other_vendor.remove(their_item)
        other_vendor.add(given)
        self.add(taken)
        return True