"""
Übung 3 - Online-Shop

In dieser Übung nutzen wir das Facade Pattern, um einen Online-Shop zu modellieren.
Der Prozess des Einkaufens kann mehrere Schritte umfassen, wie das Hinzufügen von Produkten zum Warenkorb,
das Auschecken und das Bezahlen. Ein OnlineShopFacade macht diesen Prozess einfacher und verbirgt die Komplexität.

Implementieren Sie die Klassen 'Warenkorb', 'ZahlungsService', 'InventarService' und 'OnlineShopFacade'.
"""


class Warenkorb:
    def hinzufügen(self, produkt):
        pass

    def entfernen(self, produkt):
        pass


class ZahlungsService:
    def bezahlen(self, zahlungsmethode, warenkorb):
        pass


class InventarService:
    def überprüfen_verfügbarkeit(self, produkt):
        pass


class OnlineShopFacade:
    def __init__(self):
        pass

    def kaufe_produkt(self, produkt):
        pass


if __name__ == "__main__":
    facade = OnlineShopFacade()
    facade.kaufe_produkt("Buch")
