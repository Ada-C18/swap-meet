from typing import ItemsView
from swap_meet.item import Item
class Electronics(Item):
    def __init__(self,category="Electronics", condition="0"):
        super().__init__(condition="0")

    def __str__(self) -> str:
        return "A gadget full of buttons and secrets."