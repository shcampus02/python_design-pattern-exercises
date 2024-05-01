"""
Übung 1 - Text-Dekoration

In dieser Übung werden wir das Decorator Pattern verwenden, um verschiedene Arten von Dekorationen für einen Text zu
haben, wie z.B. fetten Text, kursiven Text usw. Mit dem Decorator Pattern können wir diese Dekorationen flexibel hinzufügen
und entfernen, ohne die ursprüngliche Textklasse zu ändern.

Implementieren Sie die Klassen 'Text', 'BoldDecorator', 'ItalicsDecorator' und 'UnderlineDecorator'.
"""


class TextComponent:
    def render(self):
        pass


class Text(TextComponent):
    def render(self):
        pass


class Decorator(TextComponent):
    def __init__(self, component):
        pass


class BoldDecorator(Decorator):
    def render(self):
        pass


class ItalicsDecorator(Decorator):
    def render(self):
        pass


class UnderlineDecorator(Decorator):
    def render(self):
        pass


if __name__ == "__main__":
    test_text = Text("This is some text")
    decor_text = UnderlineDecorator(ItalicsDecorator(BoldDecorator(test_text)))
    print(decor_text.render())
