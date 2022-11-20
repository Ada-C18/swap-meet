import pytest
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_clothing_has_default_category_and_to_str():
    cloth = Clothing()
    assert cloth.category == "Clothing"
    assert str(cloth) == "The finest clothing you could wear."

def test_decor_has_default_category_and_to_str():
    decor = Decor()
    assert decor.category == "Decor"
    assert str(decor) == "Something to decorate your space."

def test_electronics_has_default_category_and_to_str():
    electronics = Electronics()
    assert electronics.category == "Electronics"
    assert str(electronics) == "A gadget full of buttons and secrets."

def test_items_have_condition_as_float():
    items = [
        Clothing(condition=3.5),
        Decor(condition=3.5),
        Electronics(condition=3.5)
    ]
    for item in items:
        assert item.condition == pytest.approx(3.5)

def test_items_have_condition_descriptions_that_are_the_same_regardless_of_type():
    items = [
        Clothing(condition=5),
        Decor(condition=5),
        Electronics(condition=5)
    ]
    five_condition_description = items[0].condition_description()
    assert isinstance(five_condition_description, str)
    for item in items:
        assert item.condition_description() == five_condition_description

    items[0].condition = 1
    one_condition_description = items[0].condition_description()
    assert isinstance(one_condition_description, str)

    for item in items:
        item.condition = 1
        assert item.condition_description() == one_condition_description

    assert one_condition_description != five_condition_description

def test_condition_description_valid():
    items = [
        Clothing(condition=0),
        Decor(condition=1),
        Electronics(condition=2),
        Clothing(condition=3),
        Decor(condition=4),
        Electronics(condition=5)
    ]

    item_1 = items[0].condition_description()
    item_2 = items[1].condition_description()
    item_3 = items[2].condition_description()
    item_4 = items[3].condition_description()
    item_5 = items[4].condition_description()
    item_6 = items[5].condition_description()

    assert items[0].condition == 0
    assert items[1].condition == 1
    assert items[2].condition == 2
    assert items[3].condition == 3
    assert items[4].condition == 4
    assert items[5].condition == 5
    assert item_1 == "You probably want a glove for this one..."
    assert item_2 == "Poor"
    assert item_3 == "Fair"
    assert item_4 == "Good"
    assert item_5 == "Excellent"
    assert item_6 == "Mint"