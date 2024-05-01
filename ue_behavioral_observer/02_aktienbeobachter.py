"""
Übung 2 - Aktienbeobachter

Das Observer-Muster kann auch für ein Aktienbeobachtungssystem nützlich sein.
Ein Aktienbeobachter kann sich für eine Aktie registrieren und erhält Updates,
wenn der Preis der Aktie sich ändert.

Implementieren Sie die Klassen 'Stock', 'StockObserver' und 'StockMarket'.
"""


class Stock:
    pass


class StockObserver:
    pass


class StockMarket:
    pass


if __name__ == "__main__":
    market = StockMarket()
    observer = StockObserver()
    market.register(observer)
    market.change_price("AAPL", 150)
    observer.update()