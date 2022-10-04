class Decor:
    def __init__(self, category ="Decor", condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return f"Something to decorate your space."

    def condition_description(self):
<<<<<<< HEAD
        return ""
=======
        return f"{self.condition}"
>>>>>>> 30ebb9904bf0ed23215518c8d1ec803c7f46d6f0
