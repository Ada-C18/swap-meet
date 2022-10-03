class Vendor:
    def __init__(self,inventory=[]):
        self.inventory = inventory
        #inventory=[]
    def get_add(self,item):
        self.item = item
        self.inventory.append(item)
        return self.item



    #attrtibute namesd inventory