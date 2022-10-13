import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#@pytest.mark.skip
def test_get_newest():
    item_a = Clothing(condition=2.0,age=6)
    item_b = Decor(condition=2.0,age=8)
    item_c = Clothing(condition=4.0,age=12)
    item_d = Decor(condition=5.0,age=2)
    item_e = Clothing(condition=3.0,age=4)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = tai.get_newest()

    assert newest_item.category == "Decor"
    assert newest_item.age == pytest.approx(2)

def test_get_newest_returns_single_item():
    item_e = Clothing(condition=3.0,age=200)
    tai = Vendor(
        inventory=[item_e]
    )

    newest_item = tai.get_newest()

    assert newest_item.category == "Clothing"
    assert newest_item.age == pytest.approx(200)

def test_get_newest_returns_none_no_inventory():
    tai = Vendor(
        inventory=[ ]
    )

    newest_item = tai.get_newest()

    assert newest_item == None

#@pytest.mark.skip
def test_get_newest_gets_first_item_with_duplicates():
    # Arrange
    item_a = Clothing(condition=2.0,age=2)
    item_b = Decor(condition=4.0,age=2)
    item_c = Electronics(condition=4.0,age=2)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    best_item = tai.get_newest()

    # Assert
    assert best_item.category == "Clothing"
    assert best_item.age == pytest.approx(2)

#@pytest.mark.skip
def test_swap_by_newest():
    # Arrange
    # me
    item_a = Decor(condition=2.0,age=1)
    item_b = Electronics(condition=4.0,age=2)
    item_c = Decor(condition=4.0,age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(condition=2.0,age=1)
    item_e = Decor(condition=4.0,age=2)
    item_f = Clothing(condition=4.0,age=3)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse)
    assert result
    assert len(tai.inventory)==3
    assert len(jesse.inventory)==3
    assert item_d in tai.inventory
    assert item_d not in jesse.inventory
    assert item_a in jesse.inventory
    assert item_a not in tai.inventory
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That the results is truthy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories, including the items which were swapped from one vendor to the other

#@pytest.mark.skip
def test_swap_by_newest_reordered():
    # Arrange
    item_a = Decor(condition=2.0,age=3)
    item_b = Electronics(condition=4.0,age=2)
    item_c = Decor(condition=4.0,age=1)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0,age=3)
    item_e = Decor(condition=4.0,age=2)
    item_f = Clothing(condition=4.0,age=1)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        jesse)
    
    #raise Exception("Complete this test according to comments below.")
    assert result
    assert len(tai.inventory)==3
    assert len(jesse.inventory)==3
    assert item_f in tai.inventory
    assert item_b in tai.inventory
    assert item_a in tai.inventory
    assert item_f not in jesse.inventory
    assert item_c in jesse.inventory
    assert item_c not in tai.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is truthy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories, and that the items that were swapped are not there

#@pytest.mark.skip
def test_swap_by_newest_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_by_newest(
        other=jesse)

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

#@pytest.mark.skip
def test_swap_by_newest_no_other_inventory_is_false():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_best_by_category(
        other=jesse)

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

#@pytest.mark.skip
def test_swap_by_newest_swaps_first_item_if_no_age():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    lai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )
    esse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse)
    other_result = lai.swap_first_item(esse)
    #raise Exception("Complete this test according to comments below.")
    assert result
    assert len(tai.inventory)==3
    assert len(jesse.inventory)==3
    assert item_a not in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in tai.inventory
    assert item_d not in jesse.inventory
    assert item_a in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
    assert jesse.inventory == esse.inventory
    assert tai.inventory == lai.inventory

    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is falsy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories