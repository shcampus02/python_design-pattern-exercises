"""
Übung 3 - Textformatierung in einer Textverarbeitung

In dieser Übung nutzen wir das Flyweight-Pattern, um verschiedene Textformatierungsstile in einer Textverarbeitung zu implementieren.
Mit dem Flyweight-Pattern können wir mehrere Instanzen pro Textformatierunsstil erstellen, ohne viel Speicherplatz zu verbrauchen.

Implementieren Sie die Klassen 'TextFormat' und 'TextFormatFactory'.
"""


class TextFormat:
    pass


class TextFormatFactory:
    pass


if __name__ == "__main__":
    factory = TextFormatFactory()
    text_format1 = factory.get_text_format('Bold')
    text_format2 = factory.get_text_format('Italic')
    text_format3 = factory.get_text_format('Bold')
    print(id(text_format1), id(text_format2),
          id(text_format3))  # Die Ids von text_format1 und text_format3 sollten gleich sein.
