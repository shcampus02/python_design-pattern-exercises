"""
Übung 2 - Grafiken darstellen

In dieser Übung erstellen wir eine Struktur, die es ermöglicht, sowohl einzelne Punkte als auch Gruppen von Punkten
als Grafiken zu behandeln. Ein Punkt hat x- und y-Koordinaten, eine Gruppe enthält eine Liste von Punkten oder anderen
Gruppen.

Implementieren Sie die Klassen `Point` und `Group`.
"""


class Graphic:
    pass

class Point(Graphic):
    pass

class Group(Graphic):
    pass



if __name__ == "__main__":
    # Hier sind einige vordefinierte Tests. Erweitern Sie Ihre Implementierung so, dass sie diese Tests bestehen.
    point1 = Point(1, 1)
    point2 = Point(2, 2)
    group = Group()
    group.add(point1)
    group.add(point2)
    # Test 1
    assert point1.get_position() == (1, 1)
    # Test 2
    assert point2.get_position() == (2, 2)
    # Test 3
    assert group.get_positions() == [(1, 1), (2, 2)]
