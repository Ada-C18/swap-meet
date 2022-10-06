# testing for swap_by_newest function
import pytest
from swap_meet.item import Item

from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest_items_returns_false():
    fatimah = Vendor(
        inventory=[]
    )

    item_d = Item(category="electronics", age = 1)
    item_e = Item(category="decor", age = 2)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert not result

def test_swap_by_newest_items_returns_true():
    item_a = Item(category="clothing", age = 2)
    item_b = Item(category="clothing", age = 1)
    item_c = Item(category="clothing", age = 3)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(category="electronics", age = 1)
    item_e = Item(category="decor", age = 2)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) == 3
    assert item_b not in fatimah.inventory
    assert item_a in fatimah.inventory
    assert item_c in fatimah.inventory
    assert item_d in fatimah.inventory
    assert len(jolie.inventory) == 2
    assert item_d not in jolie.inventory
    assert item_e in jolie.inventory
    assert item_b in jolie.inventory
    assert result