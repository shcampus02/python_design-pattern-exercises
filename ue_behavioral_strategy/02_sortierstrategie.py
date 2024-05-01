"""
Übung 2 - Sortierstrategie

Das Strategy-Muster kann auch verwendet werden, um verschiedene Sortierstrategien zu implementieren.

Implementieren Sie die Klassen 'SortingStrategy', 'QuickSortStrategy', 'MergeSortStrategy' und 'SortingContext'.
"""


class SortingStrategy:
    pass


class QuickSortStrategy(SortingStrategy):
    pass


class MergeSortStrategy(SortingStrategy):
    pass


class SortingContext:
    pass


if __name__ == "__main__":
    context = SortingContext(MergeSortStrategy())
    context.sort([4, 2, 3, 1])
    context.set_strategy(QuickSortStrategy())
    context.sort([4, 2, 3, 1])