import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_item_age_returns_correct_age():
    
    item_a = Item(age=6)
    item_b = Clothing(age=10)
    item_c = Decor(age=12)
    item_d = Electronics(age=8)

    assert item_a.age == 6
    assert item_b.age == 10
    assert item_c.age == 12
    assert item_d.age == 8


def test_swap_by_newest_returns_truthy():
    # me
    item_a = Decor(age=6)
    item_b = Electronics(age=10)
    item_c = Decor(age=12)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2)
    item_e = Decor(age=4)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert result
    assert len(tai.inventory) == len(jesse.inventory) == 3
    assert item_a not in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory
    assert item_a in jesse.inventory
    assert item_d not in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory