"""
Übung 3 - Reise Strategie

Das Strategy-Muster kann nützlich sein, um verschiedene Reisemöglichkeiten zu modellieren.

Implementieren Sie die Klassen 'TravelStrategy', 'TrainStrategy', 'BusStrategy' und 'TravelContext'.
"""


class TravelStrategy:
    pass


class TrainStrategy(TravelStrategy):
    pass


class BusStrategy(TravelStrategy):
    pass


class TravelContext:
    pass


if __name__ == "__main__":
    context = TravelContext(BusStrategy())
    context.arrange_travel("Berlin", "Munich")
    context.set_strategy(TrainStrategy())
    context.arrange_travel("Berlin", "Munich")