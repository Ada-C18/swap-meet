import pytest
from swap_meet.item import Item  # may need to delete?
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.vendor import Vendor

# `Item`s have age
# Add an `age` attribute to all `Item`s
# Implement a `Vendor` method named `swap_by_newest`, using any logic that seems appropriate

# CLARIFYING QUESTIONS:

# 1 Year/Date/Int: does this require the time library or is age just an integer?
# 2 Unknown or None age? How do we handle that?
# 3 if this is age by date, we need to return an integer to sort?
# 4 How do we want to return the value? With a string output __str__ or in list?
# 5 Can we use helper functions
# 6 Can you return a list sorted by date/age
# 7 Do we want to swap by age + category and/or age + time? Can we make this versatile?

# INPUTS/OUTPUTS:


# PSEUDOCODE:


# @pytest.mark.skip
def test_get_newest():

    # ARRANGE
    item_a = Clothing(age=5)
    item_b = Decor(age=19)
    item_c = Electronics(age=.5)
    item_d = Decor(age=123)
    item_e = Electronics(age=33)
    item_f = Clothing(age=9)
    tai = Vendor(inventory=[item_a, item_b, item_c])
    jesse = Vendor(inventory=[item_d, item_e, item_f])
# ACT
    tai_newest = tai.get_by_newest()
    jesse_newest = jesse.get_by_newest()
# ASSERT
    assert tai_newest == item_c
    assert jesse_newest == item_f


# @pytest.mark.skip
def test_swap_best_by_age():

    item_a = Clothing(age=5)
    item_b = Decor(age=19)
    item_c = Electronics(age=.5)
    tai = Vendor(inventory=[item_a, item_b, item_c])

    item_d = Decor(age=123)
    item_e = Electronics(age=33)
    item_f = Clothing(age=9)
    jesse = Vendor(inventory=[item_d, item_e, item_f])

# Act
    result = tai.swap_by_newest(
        other=jesse)

    # jesse would get item c
    # tai would get item f
    assert result == True
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c not in tai.inventory
    assert item_c in jesse.inventory

    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f not in jesse.inventory
    assert item_f in tai.inventory


# @pytest.mark.skip
def test_swap_by_newest_reordered():
    # Arrange
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(other=jesse)

    # jesse gets item c
    # tai gets
    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_a not in tai.inventory
    assert item_a in jesse.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

    assert item_d not in jesse.inventory
    assert item_d in tai.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory


# @pytest.mark.skip
def test_get_by_newest_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = jesse.get_by_newest()
    result = tai.get_by_newest()

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory


# @pytest.mark.skip
def test_swap_by_newest_no_other_inventory_is_false():
    item_a = Clothing(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Clothing(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[])

    result = tai.swap_by_newest(jesse)

    assert result == None
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0


@pytest.mark.skip
def test_return_false_invalid_age():
    pass
# ARRANGE
    item_a = Clothing(age=".5")
    item_b = Decor(age="hiya")
    item_c = Electronics(age=None)
    item_d = Decor(age="5")
    item_e = Electronics(age="!$*")
    item_f = Clothing(age=None)
    tai = Vendor(inventory=[item_a, item_b, item_c])
    jesse = Vendor(inventory=[item_d, item_e, item_f])
# ACT
    tai_newest = tai.get_by_newest()
    jesse_newest = jesse.get_by_newest()
# ASSERT
    assert tai_newest == None  # with pytest raises
    assert jesse_newest == False
