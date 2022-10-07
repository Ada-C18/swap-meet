import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#1
def test_swap_by_newest():
    #arrange
    item_a = Electronics(condition=2.0, age=1)
    item_b = Decor(condition=2.0, age=2)
    item_c = Clothing(condition=4.0, age=3)
    killian = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0, age=3)
    item_e = Decor(condition=2.0, age=2)
    item_f = Electronics(condition=4.0, age=1)
    ayla = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    #act
    killian.swap_by_newest(ayla)
    
    #assert
    assert len(killian.inventory) == 3
    assert len(ayla.inventory) ==3
    assert item_a in ayla.inventory
    assert item_f in killian.inventory


#2
def test_swap_by_newest_all_same_age_returns_1st():
    #arrange
    item_a = Electronics(condition=2.0, age=1)
    item_b = Decor(condition=2.0, age=1)
    item_c = Clothing(condition=4.0, age=1)
    killian = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0, age=1)
    item_e = Decor(condition=2.0, age=1)
    item_f = Electronics(condition=4.0, age=1)
    ayla = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    #act
    killian.swap_by_newest(ayla)
    
    #assert
    assert len(killian.inventory) == 3
    assert len(ayla.inventory) ==3
    assert item_a in ayla.inventory
    assert item_d in killian.inventory
    
#3
def test_swap_by_newest_self_no_inventory():
    #arrange
    killian = Vendor()
    

    item_d = Clothing(condition=2.0, age=1)
    item_e = Decor(condition=2.0, age=1)
    item_f = Electronics(condition=4.0, age=1)
    ayla = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    #act
    killian.swap_by_newest(ayla)
    
    #assert
    assert len(killian.inventory) == 0
    assert len(ayla.inventory) ==3
    assert item_d in ayla.inventory

