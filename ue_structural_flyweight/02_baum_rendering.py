"""
Übung 2 - Baum-Rendering in einer Landschaftsvisualisierung

In dieser Übung nutzen wir das Flyweight-Pattern, um verschiedene "Baum"-Objekte in eine Landschaftsvisualisierung einzufügen.
Mit dem Flyweight-Pattern können wir mehrere Instanzen pro "Baum"-Typ erstellen, ohne viel Speicherplatz zu belegen.

Implementieren Sie die Klassen 'Tree' und 'TreeFactory'.
"""


class Tree:
    pass


class TreeFactory:
    pass


if __name__ == "__main__":
    factory = TreeFactory()
    tree1 = factory.get_tree('Eiche')
    tree2 = factory.get_tree('Kiefer')
    tree3 = factory.get_tree('Eiche')
    print(id(tree1), id(tree2), id(tree3))  # Die Ids von tree1 und tree3 sollten gleich sein.
