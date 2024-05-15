from enum import Enum


class ProductSection(Enum):
    Others = 1
    Toys = 2
    Vehicle = 3
    Kitchen = 4
    Painting = 5
    Garden = 6
    Camping = 7
    Hiking = 8
    Men_Cloth = 9
    Women_Cloth = 10
    Boys_Cloth = 11
    Girls_Cloth = 12
    Unisex_Kids_Cloth = 13
    Unisex_Cloth = 14

    def __str__(self):
        return str(self.value)