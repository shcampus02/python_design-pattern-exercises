"""
Übung 2 - Zusätzliche Fahrzeugausstattung

In dieser Übung verwenden wir das Decorator Pattern, um ein Fahrzeug mit zusätzlichen Funktionen auszustatten.
Mit dem Decorator Pattern können wir neue Funktionen hinzufügen, ohne die ursprüngliche Fahrzeugklasse ändern zu müssen.

Implementieren Sie dazu die Klassen 'Car', 'AirConditioningDecorator', 'SoundSystemDecorator' und 'LeatherSeatsDecorator'.
"""


class VehicleComponent:
    def get_price(self):
        pass


class Car(VehicleComponent):
    def get_price(self):
        pass


class Decorator(VehicleComponent):
    def __init__(self, component):
        pass


class AirConditioningDecorator(Decorator):
    def get_price(self):
        pass


class SoundSystemDecorator(Decorator):
    def get_price(self):
        pass


class LeatherSeatsDecorator(Decorator):
    def get_price(self):
        pass


if __name__ == "__main__":
    car = Car()
    decor_car = LeatherSeatsDecorator(SoundSystemDecorator(AirConditioningDecorator(car)))
    print(decor_car.get_price())
