from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# item_a = Item(category="clothing")
# item_b = Item(category="clothing")
# item_c = Item(category="clothing")
# fatimah = Vendor(
# inventory=[item_a, item_b, item_c]
# )

# item_d = Item(category="electronics")
# item_e = Item(category="decor")
# jolie = Vendor(
#     inventory=[item_d, item_e]
# )

# items = [
#         Clothing(condition=3.5),
#         Decor(condition=3.5),
#         Electronics(condition=3.5)
#     ]
# for item in items:
#     print(item.condition)

# Arrange
# me
item_a = Decor(condition=2.0)
item_b = Electronics(condition=4.0)
item_c = Decor(condition=4.0)
tai = Vendor(
    inventory=[item_a, item_b, item_c]
)

# them
item_d = Clothing(condition=2.0)
item_e = Decor(condition=4.0)
item_f = Clothing(condition=4.0)
jesse = Vendor(
    inventory=[item_d, item_e, item_f]
)

# Act
result = tai.swap_best_by_category(
    other=jesse,
    my_priority="Clothing",
    their_priority="Decor"
)