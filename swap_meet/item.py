class Item:
    def __init__(self, category = "",condition=0):
        self.category = category
        self.condition= condition

    def __str__(self): 
        return "Hello World!" 

    def condition_description(self):
        descript_arr=["trashy", "semi-trashy", "worn out", "ok", "looking good", "good as new"]
        return descript_arr[int(self.condition)]
        #%6 is picking a number thru the range of 0-5

        
        
