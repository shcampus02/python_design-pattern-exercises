"""
Übung 2 - Restaurant

In dieser Übung nutzen wir das Facade Pattern, um ein Restaurant zu modellieren.
Ein Kunde im Restaurant muss nicht wissen, was in der Küche vor sich geht.
Ein RestaurantFacade inszeniert den Prozess der Bestellung eines Gerichtes und macht es dem Kunden einfacher.

Implementieren Sie die Klassen 'Küche', 'Kellner', 'Rechnung' und 'RestaurantFacade'.
"""


class Küche:
    def bereiten_vor(self, bestellung):
        pass


class Kellner:
    def aufnehmen_bestellung(self, gericht):
        pass

    def bringen_bestellung(self, bestellung):
        pass


class Rechnung:
    def berechne(self, bestellung):
        pass


class RestaurantFacade:
    def __init__(self):
        pass

    def bestelle_gericht(self, gericht):
        pass


if __name__ == "__main__":
    facade = RestaurantFacade()
    facade.bestelle_gericht("Pizza Margherita")
