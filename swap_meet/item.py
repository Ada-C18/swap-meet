class Item:
    def __init__(self, category = None):
        if category:
            self.category = category
        else:
            self.category = ""

    def get_by_category(category_str):
        '''
        Returns a list of Items in the inventory with given category.
        '''
        # a string with the keyword argument category
        # return list of items in that category
        
        next_item = Item(category_str)
        same_category_list = []
        if next_item.category == category_str:
            same_category_list.append(next_item)
        
            

        
