
class Vendor:
    def __init__(self, inventory=None):
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
        items_in_category = []

        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)

        return items_in_category

    def swap_items(self, vendor, my_item, their_item):

            try:
                if self.inventory and vendor.inventory:
                    me = self.inventory.index(my_item)
                    them = vendor.inventory.index(their_item)
                    self.inventory[me], vendor.inventory[them] = their_item, my_item
                    return True
            except (ValueError,IndexError,TypeError):
                return False
    
    def swap_first_item(self, vendor):
        if self.inventory and vendor.inventory:
            return self.swap_items(vendor,self.inventory[0],vendor.inventory[0])
        return False

    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        if category_list:
            category_list.sort(key=lambda item: item.condition, reverse=True)
            return category_list[0]
        return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        me = self.get_best_by_category(their_priority)
        them = other.get_best_by_category(my_priority)
        if me and them:
            self.swap_items(other, me, them)
            return True
        return False

    def get_by_newest(self):
        if self.inventory:
            return min(self.inventory, key=lambda item: item.age)
        return False


    def swap_by_newest(self, other):
        me = self.get_by_newest()
        them = other.get_by_newest()
        return self.swap_items(other,me,them)
    # def swap_by_newest_category()
