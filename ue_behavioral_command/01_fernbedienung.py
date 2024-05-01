"""
Übung 1 - Fernbedienung

In diesem Beispiel repräsentiert jede Taste auf der Fernbedienung einen Befehl. Die 'Invoker'-Klasse (Fernbedienung) führt den Befehl aus, indem sie die `execute`-Methode aufruft.

Implementieren Sie die Klassen 'Fernbedienung', 'Command', 'LichtAnCommand', 'LichtAusCommand', 'Licht'.
"""


class Fernbedienung:
    pass


class Command:
    pass


class LichtAnCommand:
    pass


class LichtAusCommand:
    pass


class Licht:
    pass


if __name__ == "__main__":
    licht = Licht()
    an_command = LichtAnCommand(licht)
    fernbedienung = Fernbedienung()
    fernbedienung.set_command(an_command)
    fernbedienung.button_press()