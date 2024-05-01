"""
Übung 4 - Softwareentwicklungsprozess

Das Template-Methoden-Muster kann verwendet werden, um einen allgemeinen Softwareentwicklungsprozess zu erstellen,
wobei die genauen Schritte in den Unterklassen definiert werden.

Implementieren Sie die Klassen 'SoftwareDevelopmentProcess', 'AgileMethodology' und 'WaterfallMethodology'.
"""


class SoftwareDevelopmentProcess:
    pass


class AgileMethodology(SoftwareDevelopmentProcess):
    pass


class WaterfallMethodology(SoftwareDevelopmentProcess):
    pass


if __name__ == "__main__":
    agile = AgileMethodology()
    agile.develop_software()
    waterfall = WaterfallMethodology()
    waterfall.develop_software()