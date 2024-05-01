"""
Übung 3 - Dateisystem

Das Visitor-Muster kann bei der Implementierung eines Dateisystems verwendet werden. Es ermöglicht verschiedene Operationen
wie das Auflisten aller Dateien, das Suchen einer bestimmten Datei, das Berechnen des gesamten verwendeten Speicherplatzes usw.

Implementieren Sie die Klassen 'FileSystemElement', 'File', 'Directory', 'FileSystemVisitor' und 'FileSystemBrowser'.
"""


class FileSystemElement:
    pass


class File(FileSystemElement):
    pass


class Directory(FileSystemElement):
    pass


class FileSystemVisitor:
    pass


class FileSystemBrowser:
    pass


if __name__ == "__main__":
    root = Directory("root")
    root.add(File("file1"))
    root.add(Directory("dir1"))
    browser = FileSystemBrowser(FileSystemVisitor())
    browser.listAllFiles(root)