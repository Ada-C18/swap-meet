class Vendor:
    def __init__(self, inventory):
        inventory = []
        self.inventory_list = inventory

    def add(self, new_item):
        return self.inventory_list.append(new_item)

    def remove(self, remove_item):
        if remove_item in self.inventory_list:
            return self.inventory_list.pop(remove_item)
        else:
            return False
