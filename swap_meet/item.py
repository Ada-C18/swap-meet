class Item:
    '''
    # Wave 2 
        def __init__(self, category = None):
            # category is the property of Item
            if category:
                self.category = category
            else:
                self.category = ""
    '''

# Wave 2 & 5
    def __init__(self, category = None):
        # category & condition are the property of Item
        #if condition:
            #self.condition = condition
        #else:
            #self.condition = ""

        self.condition = 0  

        if category:
            self.category = category
        else:
            self.category = ""


 # Wave 3
    def __str__(self):        
        return "Hello World!"

# Wave 5
    def condition_description(self, condition):
        if self.condition == 1:
            print ("Sparkling")
