import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

# @pytest.mark.skip
def test_swap_newest_item_returns_true():
    item_a = Item(age=3)
    item_b = Item(age=1)
    item_c = Item(age=5)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(age=4)
    item_e = Item(age=2)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) == 3
    assert len(jolie.inventory) == 2
    assert fatimah.inventory == [item_a, item_c, item_e] and jolie.inventory == [item_d, item_b]
    assert result


# @pytest.mark.skip
def test_swap_newest_item_from_my_empty_inventory_returns_false():
    fatimah = Vendor(
        inventory=[]
    )

    item_d = Item(age=4)
    item_e = Item(age=2)
    jolie = Vendor(
        inventory=[item_d, item_e]
    )

    result = fatimah.swap_by_newest(jolie)

    assert len(fatimah.inventory) == 0
    assert len(jolie.inventory) == 2
    assert not result


# @pytest.mark.skip
def test_swap_newest_item_from_their_empty_inventory_returns_false():
    item_a = Item(age=3)
    item_b = Item(age=1)
    item_c = Item(age=5)
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


# @pytest.mark.skip
def test_returns_false_if_age_none_in_their_inventory():
    # Arrange
    # me
    item_a = Item(age=1)
    item_b = Item(age=2)
    item_c = Item(age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Item(age=2)
    item_e = Item(age=6)
    item_f = Item(age=None)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(jesse)
    assert result == False
    assert len(tai.inventory) == 3 and len(jesse.inventory) == 3
    assert tai.inventory == [item_a, item_b, item_c] and jesse.inventory == [item_d, item_e, item_f]


# @pytest.mark.skip
def test_returns_false_if_age_none_in_my_inventory():
    # Arrange
    # me
    item_a = Item(age=None)
    item_b = Item(age=2)
    item_c = Item(age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Item(age=2)
    item_e = Item(age=6)
    item_f = Item(age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(jesse)
    assert result == False
    assert len(tai.inventory) == 3 and len(jesse.inventory) == 3
    assert tai.inventory == [item_a, item_b, item_c] and jesse.inventory == [item_d, item_e, item_f]


# @pytest.mark.skip
def test_if_multiple_same_newest_returns_first_one():
    # Arrange
    # me
    item_a = Item(age=1)
    item_b = Item(age=2)
    item_c = Item(age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Item(age=2)
    item_e = Item(age=6)
    item_f = Item(age=2)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(jesse)
    assert result == True
    assert len(tai.inventory) == 3 and len(jesse.inventory) == 3
    assert tai.inventory == [item_b, item_c, item_d] and jesse.inventory == [item_e, item_f, item_a]