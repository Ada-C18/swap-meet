import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


'''
test that all item subclasses have age accessible and that it has correct default value
test that age matches input, not just the default
test swap_by_newest:    no input, empty list, ties, ordered list input, unordered list input
'''


def test_age_attribute_in_subclasses_and_default():
    # Arrange & act
    # me
    item_a = Decor(age=15)
    item_b = Electronics(age=7)
    item_c = Clothing(age=20)
    item_d = Item(age=5)
    item_e = Item()

   


    #assert
    assert item_a.age == 15
    assert item_b.age == 7
    assert item_c.age == 20
    assert item_d.age == 5
    assert item_e.age == 0



def test_swap_by_newest_with_ordered_input():
    # Arrange
    # me
    item_a = Decor(age=15)
    item_b = Electronics(age=7)
    item_c = Decor(age=20)
    tai = Vendor(
        inventory=[item_b, item_a, item_c]
    )

    # them
    item_d = Clothing(age=13)
    item_e = Decor(age=19)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_f, item_d, item_e]
    )

    # Act
    result = tai.swap_by_newest(other=jesse)

    # Assert
    assert item_f in tai.inventory
    assert item_a in tai.inventory
    assert item_c in tai.inventory
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_b in jesse.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert result




def test_swap_by_newest_with_unordered_input():
    # Arrange
    # me
    item_a = Decor(age=15)
    item_b = Electronics(age=7)
    item_c = Decor(age=20)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=13)
    item_e = Decor(age=19)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(other=jesse)

    # Assert
    assert item_f in tai.inventory
    assert item_a in tai.inventory
    assert item_c in tai.inventory
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_b in jesse.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert result





def test_swap_by_newest_with_empty_self():
    # Arrange
    # me
    tai = Vendor(
        inventory=[]
    )

    # them
    item_d = Clothing(age=13)
    item_e = Decor(age=19)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(other=jesse)

    # Assert
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
    assert not result





def test_swap_by_newest_with_empty_other():
    # Arrange
    # me
    item_a = Decor(age=15)
    item_b = Electronics(age=7)
    item_c = Decor(age=20)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    jesse = Vendor(
        inventory=[]
    )

    # Act
    result = tai.swap_by_newest(other=jesse)

    # Assert
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert not result



def test_swap_by_newest_with_tie_in_self():
    # Arrange
    # me
    item_a = Decor(age=15)
    item_b = Electronics(age=7)
    item_c = Decor(age=7)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=4)
    item_e = Decor(age=19)
    item_f = Clothing(age=6)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(other=jesse)

    # Assert
    assert item_d in tai.inventory
    assert item_a in tai.inventory
    assert item_c in tai.inventory
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_b in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
    assert result





def test_swap_by_newest_with_tie_in_other():
    # Arrange
    # me
    item_a = Decor(age=15)
    item_b = Electronics(age=7)
    item_c = Decor(age=9)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=4)
    item_e = Decor(age=19)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(other=jesse)

    # Assert
    assert item_d in tai.inventory
    assert item_a in tai.inventory
    assert item_c in tai.inventory
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_b in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
    assert result