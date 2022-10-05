import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest_return_true():
    item_a = Clothing(age=2.0)
    item_b = Decor(age=2.0)
    item_c = Clothing(age=1.0)
    item_d = Decor(age=5.0)
    item_e = Clothing(age=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    item_f = Electronics(age=2.0)
    item_g = Decor(age=1.0)
    jolie = Vendor(
        inventory=[item_f, item_g]
    )
    
    result = tai.swap_by_newest(jolie)

    assert len(tai.inventory) == 5
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c not in tai.inventory
    assert item_d in tai.inventory
    assert len(jolie.inventory) == 2
    assert item_f in jolie.inventory
    assert item_g not in jolie.inventory
    assert result

def test_swap_newest_item_from_my_empty_returns_false():
    fatimah = Vendor(
        inventory=[]
    )

    item_d = Electronics(age=1.0)
    item_e = Decor(age=10.0)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) == 0
    assert len(jolie.inventory) == 2
    assert not result

def test_swap_first_item_from_friend_empty_returns_false():
    item_a = Clothing(age=3.0)
    item_b = Clothing(age=10.0)
    item_c = Clothing(age=8.5)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jolie = Vendor(
        inventory=[]
    )
    
    result = fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) == 3
    assert len(jolie.inventory) == 0
    assert not result