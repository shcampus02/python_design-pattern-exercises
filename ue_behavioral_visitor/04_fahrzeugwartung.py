"""
Übung 4 - Fahrzeugwartung

Das Visitor-Muster kann verwendet werden, um Wartungsservices für verschiedene Fahrzeugtypen bereitzustellen.
Jeder Service kann verschiedene Operationen durchführen, abhängig von der Art des Fahrzeugs.

Implementieren Sie die Klassen 'Vehicle', 'Car', 'Truck', 'MaintenanceVisitor' und 'MaintenanceService'.
"""


class Vehicle:
    pass


class Car(Vehicle):
    pass


class Truck(Vehicle):
    pass


class MaintenanceVisitor:
    pass


class MaintenanceService:
    pass


if __name__ == "__main__":
    vehicles = [Car(), Truck()]
    service = MaintenanceService(MaintenanceVisitor())
    service.performMaintenance(vehicles)