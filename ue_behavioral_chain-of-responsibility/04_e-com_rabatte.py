"""
Übung 4 - E-Commerce Rabatte

In einem Online-Shop könnten Rabattregeln angewendet werden, die aufeinander aufbauen. Zum Beispiel könnte es einen
Standardrabatt für alle Kunden geben, einen zusätzlichen Rabatt für VIP Kunden und einen saisonalen Rabatt, der ab einem
bestimmten Datum gilt.

Implementieren Sie eine Kette der Verantwortung, bei der jedes Glied in der Kette eine bestimmte Rabattregel anwendet.
Erstellen Sie die Klassen StandardDiscountHandler, VIPDiscountHandler und SeasonalDiscountHandler.
"""


class AbstractDiscountHandler:
    # Platz für Ihre Implementierung
    pass


class StandardDiscountHandler(AbstractDiscountHandler):
    # Platz für Ihre Implementierung
    pass


class VIPDiscountHandler(AbstractDiscountHandler):
    # Platz für Ihre Implementierung
    pass


class SeasonalDiscountHandler(AbstractDiscountHandler):
    # Platz für Ihre Implementierung
    pass


if __name__ == "__main__":
    # Hier sind einige vordefinierte Tests. Erweitern Sie Ihre Implementierung so, dass sie diese Tests bestehen.
    discount_chain = StandardDiscountHandler(VIPDiscountHandler(SeasonalDiscountHandler()))

    # Test 1
    assert discount_chain.handle("Standard", 100) == 90  # applying 10% standard discount
    # Test 2
    assert discount_chain.handle("VIP", 100) == 80  # applying 20% VIP discount
    # Test 3
    assert discount_chain.handle("Seasonal", 100) == 70  # applying 30% seasonal discount
    # Test 4
    assert discount_chain.handle("Unknown", 100) == "Invalid customer type"
