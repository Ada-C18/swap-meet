import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

def test_get_newest_item_returns_item():
    item_a = Item(age = 3)
    item_b = Item(age = 2)
    item_c = Item(age = 4)
    sam = Vendor(inventory = [item_a, item_b, item_c])

    result = sam.get_newest_item()

    assert result == item_b

def test_swap_by_newest_returns_true():
    item_a = Item(age = 3)
    item_b = Item(age = 2)
    item_c = Item(age = 4)
    sam = Vendor(inventory = [item_a, item_b, item_c])

    item_d = Item(age = 5)
    item_e = Item(age = 2)
    item_f = Item(age = 0)
    angie = Vendor(inventory = [item_d, item_e, item_f])

    result = sam.swap_by_newest(angie)

    assert result == True
    assert item_b in angie.inventory
    assert item_f in sam.inventory
    assert len(sam.inventory) == 3
    assert len(angie.inventory) == 3

def test_swap_by_newest_returns_false():
    item_a = Item(age = 3)
    item_b = Item(age = 2)
    item_c = Item(age = 4)
    sam = Vendor(inventory = [item_a, item_b, item_c])

    angie = Vendor(inventory=[])

    result = sam.swap_by_newest(angie)

    assert result == False
    assert len(angie.inventory) == 0
    assert len(sam.inventory) == 3