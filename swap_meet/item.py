# create an`Item` class
# create an attribute named `category`, which is an empty string by default
# Make category an optionally keyword argument to pass for Item 


class Item:
    def __init__(self, category=None, condition=0):
        self.category = category if category is not None else ""
        self.condition = condition if condition is not None else 0
    
    def __str__(self):
        return "Hello World!"

<<<<<<< HEAD
        
=======
    def condition_description(self, condition):
        
# - All three classes and the `Item` class have an instance method named `condition_description`, 
# which should describe the condition in words based on the value, assuming they all range from 0 to 5. 
# These can be basic descriptions 
# (eg. 'mint', 'heavily used') but feel free to have fun with these (e.g. 'You probably want a glove for this one..."). 
# The one requirement is that the `condition_description` for all three classes above have the same behavior.

<<<<<<< HEAD
        if condition == :
            return ""
        if condition == :
            return ""
        if condition == :
            return ""
        if condition == :
            return ""
        if condition == :
            return ""
        
=======
        
>>>>>>> 3bf8151819973e065f0f42cddd6430e0f0a0cbb7
>>>>>>> 8a360742e2bec8ec89a9fb58b9a4c1e61c136970
