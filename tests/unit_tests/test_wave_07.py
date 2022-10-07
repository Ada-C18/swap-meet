import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# @pytest.mark.skip
def test_swap_by_newest():
    item_a = Electronics(age = 7)
    item_b = Electronics(age = 5)
    item_c = Clothing(age = 3)
    greggington = Vendor(inventory=[item_a, item_b, item_c])

    item_d = Clothing(age = 2)
    item_e = Decor(age = 18)
    item_f = Electronics(age = 4)
    beef_loaf = Vendor(inventory=[item_d, item_e, item_f])

    result = greggington.swap_by_newest(beef_loaf)

    assert result
    assert len(greggington.inventory) == 3
    assert len(beef_loaf.inventory) == 3
    assert greggington.inventory == [item_a, item_b, item_d]
    assert beef_loaf.inventory == [item_e, item_f, item_c]

# @pytest.mark.skip
def test_swap_by_newest_with_duplicates():
    item_a = Electronics(age = 12)
    item_b = Decor(age = 8)
    item_c = Clothing(age = 8)
    moonmoonmoon = Vendor(inventory=[item_a, item_b, item_c])

    item_d = Decor(age = 6)
    item_e = Clothing(age = 1)
    item_f = Electronics(age = 4)
    item_g = Electronics(age = 15)
    radish_cake = Vendor(inventory=[item_d, item_e, item_f, item_g])

    result = moonmoonmoon.swap_by_newest(radish_cake)

    assert result
    assert len(moonmoonmoon.inventory) == 3
    assert len(radish_cake.inventory) == 4
    assert moonmoonmoon.inventory == [item_a, item_c, item_e]
    assert radish_cake.inventory == [item_d, item_f, item_g, item_b]

# @pytest.mark.skip
def test_swap_by_newest_no_inventory_is_false():
    item_a = Electronics(age = 778)
    item_b = Clothing(age = 400)
    item_c = Decor(age = 1000)
    item_d = Decor(age = 660)
    item_e = Clothing(age = 1777)
    item_f = Electronics(age = 888)

    gulliver = Vendor()
    julliver = Vendor(inventory = [item_a, item_b, item_c, item_d, item_e, item_f])
    
    result = gulliver.swap_by_newest(julliver)

    assert result == False
    assert len(gulliver.inventory) == 0
    assert len(julliver.inventory) == 6
    assert gulliver.inventory == []
    assert julliver.inventory == [item_a, item_b, item_c, item_d, item_e, item_f]

# @pytest.mark.skip
def test_swap_by_newest_no_other_inventory_is_false():
    item_a = Electronics(age = 878)
    item_b = Clothing(age = 500)
    item_c = Decor(age = 1100)
    item_d = Decor(age = 760)
    item_e = Clothing(age = 1877)
    item_f = Electronics(age = 988)

    gulliver = Vendor(inventory = [item_a, item_b, item_c, item_d, item_e, item_f])
    julliver_aka_gullivers_ex = Vendor()

    result = gulliver.swap_by_newest(julliver_aka_gullivers_ex)

    assert result == False
    assert len(gulliver.inventory) == 6
    assert len(julliver_aka_gullivers_ex.inventory) == 0
    assert gulliver.inventory == [item_a, item_b, item_c, item_d, item_e, item_f]
    assert julliver_aka_gullivers_ex.inventory == []