# The following line imports the Vendor class from the module vendor inside the swap_meet package.
import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#@pytest.mark.skip
def test_vendor_has_inventory():
    vendor = Vendor()
    assert len(vendor.inventory) == 0

#@pytest.mark.skip
def test_vendor_takes_optional_inventory():
    inventory = ["a", "b", "c"]
    vendor = Vendor(inventory=inventory)
    assert len(vendor.inventory) == 3
    assert "a" in vendor.inventory
    assert "b" in vendor.inventory
    assert "c" in vendor.inventory

#@pytest.mark.skip
def test_adding_to_inventory():
    vendor = Vendor()
    item =  Decor(age = 2, condition=4)
    result = vendor.add(item)

    assert len(vendor.inventory) == 1
    assert item in vendor.inventory
    assert result == item

#@pytest.mark.skip
def test_removing_from_inventory_returns_item():
    item = "item to remove"
    vendor = Vendor(
        inventory=["a", "b", "c", item]
    )

    result = vendor.remove(item)

    assert len(vendor.inventory) == 3
    assert item not in vendor.inventory
    assert result == item

#@pytest.mark.skip
def test_removing_not_found_is_false():
    item = "item to remove"
    vendor = Vendor(
        inventory=["a", "b", "c"]
    )

    result = vendor.remove(item)

    #raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    assert result == False
    # *********************************************************************
