"""
Übung 2 - Durchlaufen einer binären Suchstruktur

Das Iterator-Muster kann nützlich sein, wenn Sie eine Datenstruktur wie einen Binärbaum durchlaufen wollen.
In dieser Übung werden Sie einen Iterator für eine BinaryTree erstellen.

Implementieren Sie die Klassen 'BinaryTree', 'Node', 'Iterator' und 'BinaryTreeIterator'.
"""


class BinaryTree:
    pass


class Node:
    pass


class Iterator:
    pass


class BinaryTreeIterator:
    pass


if __name__ == "__main__":
    tree = BinaryTree()
    tree.add_node(Node(5))
    tree.add_node(Node(3))
    tree.add_node(Node(7))
    iterator = tree.create_iterator()
    while iterator.has_next():
        node = iterator.next()
        print(node.value)