from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.vendor import Vendor

items = [
    Clothing(condition=5),
    Item(category="Food")
]
five_condition_description = items[0].condition_description()

# returns an AttributeError
item_condition_description = items[1].condition_description()
print(item_condition_description)