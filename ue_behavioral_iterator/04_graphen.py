"""
Übung 4 - Durchlaufen eines Graphen

In dieser Übung implementieren Sie das Iterator-Muster, um einen Graphen zu durchlaufen.
Sie können eine Breitensuche (BFS) oder eine Tiefensuche (DFS) verwenden, um den Iterator zu implementieren.

Implementieren Sie die Klassen 'Graph', 'Node', 'Iterator' und 'GraphIterator'.
"""


class Graph:
    pass


class Node:
    pass


class Iterator:
    pass


class GraphIterator:
    pass


if __name__ == "__main__":
    graph = Graph()
    graph.add_node(Node("A"))
    graph.add_node(Node("B"))
    graph.add_node(Node("C"))
    iterator = graph.create_iterator()
    while iterator.has_next():
        node = iterator.next()
        print(node.value)