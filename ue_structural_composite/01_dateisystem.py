"""
Übung 1 - Dateisystem

In dieser Übung erstellen Sie eine einfache Repräsentation eines Dateisystems mit Verzeichnissen und Dateien
unter Verwendung des Composite-Musters. Eine Datei hat einen Namen und eine Größe, ein Verzeichnis hat einen Namen und
kann mehrere Dateien und Unterverzeichnisse enthalten.

Implementieren Sie die Klassen `File` und `Directory`.
"""


class FileSystemComponent:
    pass


class File(FileSystemComponent):
    pass


class Directory(FileSystemComponent):
    pass


if __name__ == "__main__":
    # Hier sind einige vordefinierte Tests. Erweitern Sie Ihre Implementierung so, dass sie diese Tests bestehen.
    file1 = File("File1", 100)
    file2 = File("File2", 200)
    directory = Directory("Directory")
    directory.add(file1)
    directory.add(file2)

    # Test 1
    assert file1.get_size() == 100
    # Test 2
    assert file2.get_size() == 200
    # Test 3
    assert directory.get_size() == 300
