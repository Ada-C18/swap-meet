from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            inventory=[]
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

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory:
            if their_item in friend.inventory:
                self.remove(my_item)
                friend.add(my_item)
                friend.remove(their_item)
                self.add(their_item)
                
                return True
            else:
                return False 
        else:
            return False
    
    def swap_first_item(self, friend):
        if len(self.inventory)== 0 or len(friend.inventory)== 0:
            return False
        
        my_item= self.inventory[0]
        friend_item= friend.inventory[0]

        self.swap_items(friend,my_item,friend_item)
        
        return True

    def get_best_by_category(self, category):

        item_list = self.get_by_category(category)
        if len(item_list) == 0:
            return None 
        else:
            best_item= item_list[0]
            for item in item_list:
                if item.condition > best_item.condition:
                    best_item = item
            
            return best_item 

    def swap_best_by_category(self, other, my_priority, their_priority):

        my_item = self.get_best_by_category(their_priority)
        other_item= other.get_best_by_category(my_priority)
        if my_item == None or other_item == None:
            return False 
        
        return self.swap_items(other,my_item, other_item)


        




        
        # higest_condition= item.condition[0]
        # for item in self.inventory:
        #     if item.condtion >= higest_condition:
        #         higest_condition.append(item.condition)









        

