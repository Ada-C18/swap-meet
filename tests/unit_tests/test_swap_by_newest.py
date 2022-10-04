import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_get_newest_returns_correct_item():
    item_a = Decor(condition=2.0, age=3)
    item_b = Electronics(condition=4.0, age=2)
    item_c = Decor(condition=4.0, age=1)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.get_newest()

    assert result == item_c
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

def test_get_newest_returns_false_for_empty_list():
    jesse = Vendor(inventory=[])

    result = jesse.get_newest()

    assert result == False
    assert len(jesse.inventory) == 0
    
def test_swap_newest_swaps_correct_items():
    # Arrange
    # me
    item_a = Decor(condition=2.0, age=3)
    item_b = Electronics(condition=4.0, age=2)
    item_c = Decor(condition=4.0, age=1)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(condition=2.0, age=3)
    item_e = Decor(condition=4.0, age=10)
    item_f = Clothing(condition=4.0, age=2)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(other=jesse)

    # raise Exception("Complete this test according to comments below.")
    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_f in tai.inventory
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_c in jesse.inventory

# @pytest.mark.skip
def test_swap_by_newest_reorder():
    # Arrange
    # me
    item_a = Decor(condition=2.0, age= 3)
    item_b = Electronics(condition=4.0, age=1)
    item_c = Decor(condition=4.0, age=3)
    tai = Vendor(
        inventory=[item_c, item_a, item_b]
    )

    # them
    item_d = Clothing(condition=2.0, age=3)
    item_e = Decor(condition=4.0, age=1)
    item_f = Clothing(condition=4.0, age=2)
    jesse = Vendor(
        inventory=[item_e, item_f, item_d]
    )

    # Act
    result = tai.swap_by_newest(other=jesse)

    # raise Exception("Complete this test according to comments below.")
    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_e in tai.inventory
    assert item_a in tai.inventory
    assert item_c in tai.inventory
    assert item_d in jesse.inventory
    assert item_f in jesse.inventory
    assert item_b in jesse.inventory

def test_swap_newest_with_empty_inventory_is_false():
    # Arrange
    item_a = Decor(condition=2.0, age=1)
    item_b = Electronics(condition=4.0, age=2)
    item_c = Decor(condition=4.0, age=3)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    jesse = Vendor(
        inventory=[]
    )

    # Act
    result = tai.swap_by_newest(other=jesse)

    # raise Exception("Complete this test according to comments below.")
    assert result == False
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory