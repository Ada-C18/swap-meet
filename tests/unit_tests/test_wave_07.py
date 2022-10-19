import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_get_newest():
    item_a = Clothing(age = 1.0)
    item_b = Decor(condition = 3.5, age = 8.0)
    item_c = Electronics(condition = 2.0, age = 0.5)
    amy = Vendor(inventory=[item_a, item_b, item_c])
    
    newest_item = amy.get_newest()

    assert newest_item is item_c

def test_get_newest_none_age_specified_is_None():
    item_a = Clothing(condition = 0.0)
    item_b = Clothing(condition = 1.0)
    item_c = Clothing(condition = 2.0)
    amy = Vendor(inventory=[item_a, item_b, item_c])
    
    newest_item = amy.get_newest()

    assert not newest_item

def test_swap_by_newest():
    item_a = Clothing(age = 1.0)
    item_b = Decor(condition = 3.5, age = 8.0)
    item_c = Electronics(condition = 2.0, age = 0.5)
    amy = Vendor(inventory=[item_a, item_b, item_c])

    item_d = Clothing()
    item_e = Decor(condition = 3.5, age = 2.0)
    item_f = Electronics(condition = 2.0, age = 5.0)
    yun = Vendor(inventory=[item_d, item_e, item_f])

    result = amy.swap_by_newest(yun)

    assert result
    assert len(amy.inventory) == 3
    assert len(yun.inventory) == 3
    assert item_b in amy.inventory
    assert item_a in amy.inventory
    assert item_e in amy.inventory
    assert item_c not in amy.inventory
    assert item_d in yun.inventory
    assert item_f in yun.inventory
    assert item_c in yun.inventory
    assert item_e not in yun.inventory

def test_swap_by_newest_no_inventory_is_false():
    amy = Vendor(inventory=[])

    item_a = Clothing(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Clothing(age=4.0)
    yun = Vendor(inventory=[item_a, item_b, item_c])

    result = amy.swap_by_newest(yun)

    assert not result
    assert len(amy.inventory) == 0
    assert len(yun.inventory) == 3
    assert item_a in yun.inventory
    assert item_b in yun.inventory
    assert item_c in yun.inventory

def test_swap_by_newest_other_none_age_specified_is_false():
    item_a = Clothing(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Clothing(age=4.0)
    amy = Vendor(inventory=[item_a, item_b, item_c])

    item_d = Clothing(condition = 0.0)
    item_e = Clothing(condition = 1.0)
    item_f = Clothing(condition = 2.0)
    yun = Vendor(inventory=[item_d, item_e, item_f])

    result = amy.swap_by_newest(yun)

    assert not result
    assert len(amy.inventory) == 3
    assert len(yun.inventory) == 3
    assert item_a in amy.inventory
    assert item_b in amy.inventory
    assert item_c in amy.inventory
    assert item_d in yun.inventory
    assert item_e in yun.inventory
    assert item_f in yun.inventory
