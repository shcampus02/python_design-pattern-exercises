"""
Übung 1 - Computer

In dieser Übung nutzen wir das Facade Pattern, um einen Computer zu modellieren.
Der Computer kann viele verschiedene Teile haben, und es kann kompliziert sein, jeden einzeln anzusprechen.
Mit einem ComputerFacade können wir diese Komplexität verbergen und das Hoch- und Herunterfahren des Computers einfacher gestalten.

Implementieren Sie die Klassen 'CPU', 'Memory', 'HardDrive' und 'ComputerFacade'.
"""


class CPU:
    def freeze(self):
        pass

    def execute(self):
        pass


class Memory:
    def load(self, position, data):
        pass


class HardDrive:
    def read(self, lba, size):
        pass


class ComputerFacade:
    def __init__(self):
        pass

    def start(self):
        pass


if __name__ == "__main__":
    facade = ComputerFacade()
    facade.start()
