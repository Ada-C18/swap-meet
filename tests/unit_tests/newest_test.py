import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.item import Item

@pytest.mark.skip
def test_get_newest():
    item_a = Item(age=10)
    item_b = Item(age=40)
    item_c = Item(age=6)
    
    vendor = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    items = vendor.get_newest(vendor)

    assert len(items) == 1
    # assert item_a in items
    # assert item_c in items
    # assert item_b not in items
