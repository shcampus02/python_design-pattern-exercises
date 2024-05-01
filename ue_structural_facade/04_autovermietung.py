"""
Übung 4 - Autovermietung

In dieser Übung nutzen wir das Facade Pattern, um einen Autoverleihprozess zu modellieren.
Der Prozess kann mehrere Schritte umfassen: Verfügbarkeit kontrollieren, Auto buchen und bezahlen.
Eine AutovermietungsFacade macht diesen Prozess einfacher und verbirgt die Komplexität der Schritte.

Implementieren Sie die Klassen 'Inventar', 'Fahrzeuge', 'Rechnung' und 'AutovermietungsFacade'.
"""


class Inventar:
    def check_verfuegbarkeit(self, fahrzeugtyp, daten):
        pass


class Fahrzeuge:
    def buche_auto(self, fahrzeugtyp, daten):
        pass


class Rechnung:
    def bezahlen(self, fahrzeug, daten):
        pass


class AutovermietungsFacade:
    def __init__(self):
        pass

    def vermiete_auto(self, fahrzeugtyp, daten):
        pass


if __name__ == "__main__":
    facade = AutovermietungsFacade()
    facade.vermiete_auto("SUV", ("01-10-2023", "15-10-2023"))
