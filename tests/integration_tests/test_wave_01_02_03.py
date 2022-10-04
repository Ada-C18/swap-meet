import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

# @pytest.mark.skip
@pytest.mark.integration_test
def test_integration_wave_01_02_03():
    # make a vendor  
    vendor = None
    vendor = Vendor()
    print(len(vendor.inventory))
    assert len(vendor.inventory) == 0

    # add an item
    item1 = Item(category="Clothing")
    item2 = Item(category="Electronics")
    result1 = vendor.add(item1)
    result2 = vendor.add(item2)

    assert len(vendor.inventory) == 2
    assert item1 in vendor.inventory
    assert item2 in vendor.inventory
    assert result1 == item1
    assert result2 == item2

    # remove an item
    remove_result = vendor.remove(item1)

    assert len(vendor.inventory) == 1
    assert item1 not in vendor.inventory
    assert remove_result == item1

    # get item by category, truthy
    items = vendor.get_by_category("Electronics")
    print(f"🌼 01 {len(vendor.inventory)}")

    assert len(items) == 1
    assert item2 in items

    # get item by category, falsy
    items = vendor.get_by_category("Clothing")
    print(f"🌼 02 {len(vendor.inventory)}")
    assert len(items) == 0
    print(f"🌼 03 {len(vendor.inventory)}")
    other_vendor = Vendor()
    print(f"{vendor} vs. {other_vendor}")
    print(f"🌼 04a {len(vendor.inventory)}")
    print(f"🌼 04b {len(other_vendor.inventory)}")

    # swap items
    item3 = Item(category="Decor")
    print(f"🌼 05a vi: {len(vendor.inventory)} vs. ovi: {len(other_vendor.inventory)}")
    other_vendor.add(item3)
    print(f"🌼 05b vi: {len(vendor.inventory)} vs. ovi: {len(other_vendor.inventory)}")
    
    print(f"🌼 06 {len(vendor.inventory)}")

    vendor.swap_items(other_vendor, item2, item3)



    assert len(vendor.inventory) == 1
    assert len(other_vendor.inventory) == 1
    assert item2 in other_vendor.inventory
    assert item3 in vendor.inventory


