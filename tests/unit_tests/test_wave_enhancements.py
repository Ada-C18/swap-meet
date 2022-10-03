import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

@pytest.mark.skip
def test_swap_by_newest():
    # Arrange
    # me
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=1.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse
    )

    # raise Exception("Complete this test according to comments below.")
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert jesse.inventory[-1] == item_c
    assert jesse.inventory[0] == item_d
    assert jesse.inventory[1] == item_e
    assert tai.inventory[1] == item_b
    assert tai.inventory[0] == item_a
    assert tai.inventory[-1] == item_f
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That the results is truthy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories, including the items which were swapped from one vendor to the other
