import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# @pytest.mark.skip
def test_get_newest():
    #Arrange
    item_a = Decor(year_created=2010)
    item_b = Electronics(year_created=2005)
    item_c = Decor(year_created=2017)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    #Act
    result = tai.get_newest()

    #Assert
    assert result == item_c



# @pytest.mark.skip
def test_swap_by_newest():
    # Arrange
    # me
    item_a = Decor(year_created=2010)
    item_b = Electronics(year_created=2005)
    item_c = Decor(year_created=2017)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(year_created=2005)
    item_e = Decor(year_created=2010)
    item_f = Clothing(year_created=2020)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    tai.swap_by_newest(jesse)

    # raise Exception("Complete this test according to comments below.")
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert jesse.inventory[2] == item_c
    assert jesse.inventory[0] == item_d
    assert jesse.inventory[1] == item_e
    assert tai.inventory[1] == item_b
    assert tai.inventory[0] == item_a
    assert tai.inventory[2] == item_f
