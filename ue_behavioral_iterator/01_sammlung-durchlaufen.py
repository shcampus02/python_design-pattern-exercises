"""
Übung 1 - Durchlaufen einer Sammlung

Das Iterator-Muster bietet ein gemeinsames Interface für das Durchlaufen von Elementen verschiedener Sammlungen.
In dieser Übung werden Sie einen Iterator für eine Buchsammlung erstellen.

Implementieren Sie die Klassen 'BookCollection', 'Book', 'Iterator' und 'BookIterator'.
"""


class BookCollection:
    pass


class Book:
    pass


class Iterator:
    pass


class BookIterator:
    pass


if __name__ == "__main__":
    collection = BookCollection()
    collection.add_book(Book("Moby Dick"))
    collection.add_book(Book("War and Peace"))
    iterator = collection.create_iterator()
    while iterator.has_next():
        book = iterator.next()
        print(book.title)