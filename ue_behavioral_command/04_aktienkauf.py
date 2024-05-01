"""
Übung 4 - Aktienkaufsystem

In diesem Szenario könnte jede Art von Transaktion (Kauf, Verkauf) als Command in einem Aktienhandelssystem dargestellt werden.

Implementieren Sie die Klassen 'Aktienhandel', 'Command', 'KaufenCommand', 'VerkaufenCommand', 'Aktie'.
"""


class Aktienhandel:
    pass


class Command:
    pass


class KaufenCommand:
    pass


class VerkaufenCommand:
    pass


class Aktie:
    pass


if __name__ == "__main__":
    aktie = Aktie("Microsoft", 10)
    kaufen_command = KaufenCommand(aktie)
    aktienhandel = Aktienhandel()
    aktienhandel.set_command(kaufen_command)
    aktienhandel.transaktion_ausfuehren()