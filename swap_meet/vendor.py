from types import MemberDescriptorType

#from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = None):

        self.inventory = inventory if inventory is not None else []
        
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        return [item for item in self.inventory if category == item.category]
        # items_list = []
        # for item in self.inventory:
        #     if category == item.category:
        #         items_list.append(item)
        # return items_list

    def different_vendor():
        #composite/component relationship
        pass

    def swap_items(self, different_vendor(), my_item, their_item):
        pass
