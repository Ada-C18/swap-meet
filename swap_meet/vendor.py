class Vendor:
   def __init__(self, inventory=None):
      self.inventory = inventory if inventory is not None else []

   #adds an item to the inventory
   def add(self, item):
      self.inventory.append(item)
      return item

   #removes an item from the inventory
   def remove(self, item):
      if item not in self.inventory:
            return False
      self.inventory.remove(item)
      return item

   # takes one argument (string => category) and returns a list of items in the 
   # in the inventory with that category
   def get_by_category(self, category):
      all_items = []
      for item in self.inventory:
         if item.category == category:
            all_items.append(item) 
      return all_items
