class Item:
    def __init__(self,category="",condition=0):
        self.category=category
        self.condition=condition
    
    def __str__(self):
        print(self.category)
        return "Hello World!"

    def condition_description(self):
        return_key=self.condition//1
        condition_dict={
            1:"Do not swap",
            2:"Maybe, but probably not",
            3:"I suppose it's ok",
            4:"Yeah, sure",
            5:"Nice"
        }
        """if self.condition<1.5:
            phrase="Do not swap"
        elif self.condition<2.5:
            phrase="Maybe, but probably not"
        elif self.condition<3.5:
            phrase="I suppose it's ok"
        elif self.condition<4.5:
            phrase="Yeah,sure"
        else:
            phrase="Nice" """
        return condition_dict[return_key]
