"""
Übung 1 - Symbols in a Anwendung

In dieser Übung nutzen wir das Flyweight-Pattern, um "Icons" in eine Computer-Anwendung einzufügen.
Mit dem Flyweight-Pattern können wir mehrere Instanzen eines bestimmten "Icon"-Objekts erstellen, ohne das Gedächtnis überzuladen.

Implementieren Sie die Klassen 'Icon' und 'IconFactory'.
"""


class Icon:
    pass


class IconFactory:
    pass


if __name__ == "__main__":
    factory = IconFactory()
    icon1 = factory.get_icon('file')
    icon2 = factory.get_icon('folder')
    icon3 = factory.get_icon('file')
    print(id(icon1), id(icon2), id(icon3))  # Die Ids von icon1 und icon3 sollten gleich sein.
