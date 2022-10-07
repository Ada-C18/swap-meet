class Item:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            description = "This ain't it, chief"
        elif 0 < self.condition < 1.5:
            description = "Probably not cursed!"
        elif 1.5 < self.condition < 3:
            description = "Could be worse"
        elif 3 < self.condition < 4.5:
            description = "Pretty sweet"
        elif 4.5 < self.condition <= 5:
            description = "I can't believe it's not new!"
        return description

    
    