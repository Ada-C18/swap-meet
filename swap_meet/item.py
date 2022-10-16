# from swap_meet.vendor import Vendor

################################## Wave 2 ##################################
class Item:
    def __init__(self,category = "",condition = 0):
        """Expectation: each Item will have an attribute named category, which is an empty string by default
        When we initialize an instance of Item, we can optionally pass in a string with the keyword argument category 
        Wave 5 asks: All three classes and the Item class have an attribute called condition, which can be optionally provided in the initializer. The default value should be 0
        """
        
        self.category = category
        self.condition = condition 
        

################################## Wave 3 ##################################
    def __str__(self):
        """ Expectation: write a method to stringify an Item using str(). When we stringify (convert to a string) an instance of Item using str()
        Ouput: returns "Hello World!"
        """
        
        return ("Hello World!")


################################## Wave 5 ##################################


    def condition_description(self):
        """Expectation: All three classes and the Item class have an instance method named condition_description, which should describe the condition in words based on the value, assuming they all range from 0 to 5.
        The one requirement is that the condition_description for all three classes above have the same behavior. 
        Input: condition rate ranges from 0 to 5
        Output: return associated condition description
        """

        
        if self.condition <=2:
            return f"Fair condition:{round(self.condition,1)}"
        elif self.condition <=3:
            return f"Good condition: {round(self.condition,1)}"
        elif self.condition <=4:
            return f"Great condition: {round(self.condition,1)}"
        else:
            return f"Excellent condition: {round(self.condition,1)}"
