import pytest
from swap_meet.item import Item
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_item_has_age_as_float():
    items = [
        Clothing(age=10.5),
        Decor(age=10.5),
        Electronics(age=10.5)
    ]
    for item in items:
        assert item.age == pytest.approx(10.5)

def test_get_newest():
    item_a = Clothing(age=10.5)
    item_b = Decor(age=0)
    item_c = Electronics(age=6)
    fatimah = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    
    newest = fatimah.get_newest()