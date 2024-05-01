"""
Übung 3 - Mediator für Flugverkehrsleitsystem

In einem Flugverkehrsleitsystem kann das Mediator-Muster verwendet werden, um
die Kommunikation zwischen verschiedenen Flugzeugen zu steuern. Das Flugverkehrsleitsystem (Mediator)
verwaltet die Kommunikation und stellt sicher, dass Nachrichten korrekt zwischen Flugzeugen übertragen werden.

Implementieren Sie die Klassen 'ATCMediator', 'Airplane' und 'SpecificAirplane'.
"""


class ATCMediator:
    pass


class Airplane:
    pass


class SpecificAirplane:
    pass


if __name__ == "__main__":
    mediator = ATCMediator()
    airplane1 = SpecificAirplane(mediator, "Airplane 1")
    airplane2 = SpecificAirplane(mediator, "Airplane 2")
    mediator.register(airplane1)
    mediator.register(airplane2)
    airplane1.send("Hello Airplane 2")  # This will send a message to Airplane 2 through the ATCMediator