"""
Übung 3 - Bauplan

Das Template-Methoden-Muster kann verwendet werden, um einen Bauplan zu erstellen,
wobei die genauen Schritte in den Unterklassen definiert werden.

Implementieren Sie die Klassen 'BuildingBlueprint', 'HouseBlueprint' und 'ApartmentBlockBlueprint'.
"""


class BuildingBlueprint:
    pass


class HouseBlueprint(BuildingBlueprint):
    pass


class ApartmentBlockBlueprint(BuildingBlueprint):
    pass


if __name__ == "__main__":
    house_blue = HouseBlueprint()
    house_blue.build()
    apartment_blue = ApartmentBlockBlueprint()
    apartment_blue.build()