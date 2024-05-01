"""
Übung 1 - GeoFormen rendern

Im Kontext eines Rendering-Systems kann das Visitor-Muster angewendet werden, um verschiedene Arten von
Geometrieobjekten (wie Kreise, Rechtecke usw.) zu behandeln und deren Renderlogik dynamisch zu ändern.

Implementieren Sie die Klassen 'Shape', 'Circle', 'Rectangle', 'ShapeRenderer' und 'RenderVisitor'.
"""


class Shape:
    pass


class Circle(Shape):
    pass


class Rectangle(Shape):
    pass


class RenderVisitor:
    pass


class ShapeRenderer:
    pass


if __name__ == "__main__":
    shapes = [Circle(), Rectangle()]
    renderer = ShapeRenderer(RenderVisitor())
    renderer.renderShapes(shapes)