class Item:
    def __init__(self,category="",condition=0):
        self.category=category
        self.condition=condition
    
    def __str__(self):
        print(self.category)
        return "Hello World!"

    def condition_description(self):
        phrase=""
        if self.condition<2.5:
            phrase="Do not swap"
        elif self.condition<4:
            "I suppose it's ok"
        else:
            "Nice"
        return phrase
