"""
Übung 2 - Steuerberechnung

Wenn es mehrere Arten von Produkten gibt und für jedes Produkt verschiedene Steuersätze gelten,
kann das Visitor-Design-Muster nützlich sein, um den korrekten Steuersatz auf jedes Produkt anzuwenden.

Implementieren Sie die Klassen 'Product', 'FoodProduct', 'ElectronicsProduct', 'TaxVisitor' und 'CheckoutSystem'.
"""


class Product:
    pass


class FoodProduct(Product):
    pass


class ElectronicsProduct(Product):
    pass


class TaxVisitor:
    pass


class CheckoutSystem:
    pass


if __name__ == "__main__":
    products = [FoodProduct(), ElectronicsProduct()]
    checkout = CheckoutSystem(TaxVisitor())
    total = checkout.calculateTotal(products)
    print("Total cost: ", total)