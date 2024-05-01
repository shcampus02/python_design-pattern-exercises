"""
Übung 3 - Verschiedene Arten von Pizza

In dieser Übung nutzen wir das Decorator-Pattern, um verschiedene Arten von Belägen für eine Pizza hinzufügen zu können.
Mit dem Decorator-Pattern können wir flexibel neue Beläge hinzufügen, ohne die ursprüngliche Pizza-Klasse ändern zu müssen.

Implementieren Sie die Klassen 'Pizza', 'CheeseDecorator', 'TomatoDecorator' und 'HamDecorator'.
"""


class PizzaComponent:
    def get_cost(self):
        pass


class Pizza(PizzaComponent):
    def get_cost(self):
        pass


class Decorator(PizzaComponent):
    def __init__(self, component):
        pass


class CheeseDecorator(Decorator):
    def get_cost(self):
        pass


class TomatoDecorator(Decorator):
    def get_cost(self):
        pass


class HamDecorator(Decorator):
    def get_cost(self):
        pass


if __name__ == "__main__":
    pizza = Pizza()
    decor_pizza = HamDecorator(TomatoDecorator(CheeseDecorator(pizza)))
    print(decor_pizza.get_cost())
