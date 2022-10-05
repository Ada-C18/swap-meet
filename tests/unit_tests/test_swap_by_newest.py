import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest_returns_false():
    item_a = Item(category="electronics", age = 1)
    item_b = Item(category="decor", age = 3)
    jolie = Vendor(
        inventory=[item_a, item_b]
    )
    item_d = Item(category="electronics", age = 3)
    item_e = Item(category="decor", age = 1)
    fatimah = Vendor(
        inventory=[item_d, item_e]
    )
    
    result = fatimah.swap_by_newest(jolie)
    
    assert result is True
    assert len(fatimah.inventory) == 2
    assert len(jolie.inventory) == 2
    assert item_e in jolie.inventory
    assert item_a in fatimah.inventory