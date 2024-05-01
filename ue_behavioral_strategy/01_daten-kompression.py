"""
Übung 1 - Daten Kompression

Das Strategy-Muster kann verwendet werden, um verschiedene Datenkompressionsalgorithmus
zu implementieren und zur Laufzeit einen davon auszuwählen.

Implementieren Sie die Klassen 'CompressionStrategy', 'ZipCompressionStrategy', 'RarCompressionStrategy' und 'CompressionContext'.
"""


class CompressionStrategy:
    pass


class ZipCompressionStrategy(CompressionStrategy):
    pass


class RarCompressionStrategy(CompressionStrategy):
    pass


class CompressionContext:
    pass


if __name__ == "__main__":
    context = CompressionContext(RarCompressionStrategy())
    context.create_archive("myData")
    context.set_strategy(ZipCompressionStrategy())
    context.create_archive("myData")