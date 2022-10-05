from tokenize import String
from types import MemberDescriptorType
from swap_meet.item import Item


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

    def swap_items(self, friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False

        self.add(their_item)
        friend.add(my_item)
        self.remove(my_item)
        friend.remove(their_item)

        return True