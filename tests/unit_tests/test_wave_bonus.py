import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_get_age():

    # Arrange
    item_a = Clothing(age=2)
    item_b = Decor(age=2)
    item_c = Clothing(age=4)
    item_d = Decor(age=5)
    item_e = Clothing(age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = tai.get_by_age()

    assert len(newest_item) == 5
    assert item_a in newest_item
    

def test_swap_by_newest():
    item_a = Decor(age=2) #
    item_b = Electronics(age=3) 
    item_c = Decor(age=4) 
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=1) #
    item_e = Decor(age=6) 
    item_f = Clothing(age=5) 
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    result = tai.swap_by_newest(jesse)

    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_d in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_a in jesse.inventory
    assert item_f in jesse.inventory
    assert item_e in jesse.inventory

def test_empty_inventory_returns_false():
    item_a = Decor(age=2) #
    item_b = Electronics(age=3) 
    item_c = Decor(age=4) 
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    
    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_by_newest(jesse)

    assert result == False
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    