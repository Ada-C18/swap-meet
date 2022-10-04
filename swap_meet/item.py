class Item:
    def __init__(self,category="",condition=0, age=0):
        self.category=category
        self.condition=condition
        self.age=age
    
    def __str__(self):
        print(self.category)
        return "Hello World!"

    def condition_description(self):
        return_key=self.condition//1
        condition_dict={
            0:"Gross",
            1:"Do not swap",
            2:"Maybe, but probably not",
            3:"I suppose it's ok",
            4:"Yeah, sure",
            5:"Nice"
        }
        return condition_dict[return_key]
