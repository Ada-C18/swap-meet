from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = []):

        self.inventory=inventory
    
    def add(self,new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, removed_item):
        if removed_item not in self.inventory:
            return False
        else:
            self.inventory.remove(removed_item)
            return removed_item

    def get_by_category(self, category):
        item_list=[]
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)

        return item_list


        

