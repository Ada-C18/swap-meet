import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest():
    # Arrange
    # me
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(jesse)
    tai_new_inventory = [item_c, item_b, item_d]
    jesse_new_inventory = [item_a, item_f, item_e]


    assert result is True
    assert len(tai.inventory) == 3 and len(jesse.inventory) == 3
    for item in jesse_new_inventory:
        assert item in jesse.inventory
    for item in tai_new_inventory:
        assert item in tai.inventory