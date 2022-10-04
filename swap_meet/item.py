class Item:
    def __init__(self, category = '', condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return f"Hello World!"

    def condition_description(self):
<<<<<<< HEAD
        return f""
=======
        return f"{self.condition}"
>>>>>>> 30ebb9904bf0ed23215518c8d1ec803c7f46d6f0
