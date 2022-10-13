class Vendor:
    def __init__(self,inventory=None):
        self.inventory=inventory or []

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
    
    def swap_first_item(self,other_vendor):
        if not len(self.inventory) or not len(other_vendor.inventory):
            return False
        self.swap_items(other_vendor,self.inventory[0],other_vendor.inventory[0])
        #self.add(other_vendor.inventory.pop(0))
        #other_vendor.add(self.inventory.pop(0))
        return True

    def get_best_by_category(self,category):
        cat_list=self.get_by_category(category)
        if not cat_list:
            return None
        print(cat_list)
        return max(cat_list,key=lambda x:x.condition)
    
    def swap_best_by_category(self,other="", my_priority="", their_priority=""):
        my_trade_item=self.get_best_by_category(their_priority)
        other_trade_item=other.get_best_by_category(my_priority)
        if not my_trade_item or not other_trade_item:
            return False
        self.swap_items(other,my_trade_item,other_trade_item)
        return True
    
    def get_newest(self):
        newest_thing=None
        smallest_age=100000000
        for item in self.inventory:
            if item.age<smallest_age:
                smallest_age=item.age
                newest_thing=item
        return newest_thing

    def swap_by_newest(self, other):
        my_newest=self.get_newest()
        their_newest=other.get_newest()
        if not my_newest or not their_newest:
            return False
        self.swap_items(other,my_newest,their_newest)
        return True
