"""
Übung 2 - Texteditor

In diesem Beispiel fungiert jeder Befehl als eine Operation im Texteditor (zum Beispiel Schreiben, Löschen, Kopieren, Einfügen usw.). Der 'Invoker'-Klasse (Texteditor) ermöglicht dem Benutzer das Ausführen und Rückgängigmachen von Befehlen.

Implementieren Sie die Klassen 'Texteditor', 'Command', 'SchreibenCommand', 'LöschenCommand', 'Text'.
"""


class Texteditor:
    pass


class Command:
    pass


class SchreibenCommand:
    pass


class LöschenCommand:
    pass


class Text:
    pass


if __name__ == "__main__":
    text = Text()
    schreib_command = SchreibenCommand(text, "Hallo Welt")
    editor = Texteditor()
    editor.set_command(schreib_command)
    editor.aktion_ausfuehren()