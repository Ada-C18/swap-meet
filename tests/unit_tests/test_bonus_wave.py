import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_successfully_swaps_newest_items():
    # Arrange
    item_a = Clothing(age=2)
    item_b = Decor(age=4)
    item_c = Electronics(age=1)
    item_d = Decor(age=3)
    lily = Vendor(
        [item_a, item_b]
        )
    george = Vendor(
        [item_c, item_d]
        )
    # Act
    result = lily.swap_by_newest(george)
    # Assert
    assert result
    assert len(lily.inventory) == 2
    assert len(george.inventory) == 2
    assert item_c in lily.inventory
    assert item_b in lily.inventory
    assert item_a in george.inventory
    assert item_d in george.inventory

def test_swaps_first_items_if_age_is_a_tie():
    # Arrange
    item_a = Clothing(age=2)
    item_b = Decor(age=2)
    item_c = Electronics(age=6)
    item_d = Decor(age=3)
    lily = Vendor(
        [item_a, item_b]
        )
    george = Vendor(
        [item_c, item_d]
        )
    # Act
    result = lily.swap_by_newest(george)
    # Assert
    assert result
    assert len(lily.inventory) == 2
    assert len(george.inventory) == 2
    assert item_d in lily.inventory
    assert item_b in lily.inventory
    assert item_a in george.inventory
    assert item_c in george.inventory

@pytest.mark.skip
def test_swap_newest_item_no_inventory_is_false():
    # Arrange
    item_a = Clothing(age=2)
    item_b = Decor(age=1)
    lily = Vendor(
        [item_a, item_b]
        )
    george = Vendor(

    )
    # Act
    result = lily.swap_by_newest(george)
    # Assert
    assert not result
    assert len(lily.inventory) == 2
    assert not george.inventory
    assert item_a in lily.inventory
    assert item_b in lily.inventory

@pytest.mark.skip
def test_swap_newest_item_no_inventory_is_false_reversed():
    # Arrange
    item_c = Electronics(age=1)
    item_d = Decor(age=3)
    lily = Vendor(
        
    )
    george = Vendor(
        [item_c, item_d]
        )
    # Act
    result = lily.swap_by_newest(george)
    # Assert
    assert not result
    assert not lily.inventory
    assert len(george.inventory) == 2
    assert item_c in george.inventory
    assert item_d in george.inventory