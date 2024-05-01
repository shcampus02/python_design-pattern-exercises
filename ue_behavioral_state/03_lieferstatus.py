"""
Übung 3 - Lieferstatus

In dieser Übung verfolgen Sie den Status einer Lieferung, die verschiedene Zustände durchlaufen kann.

Implementieren Sie die Klassen 'DeliveryStatus', 'OrderReceivedStatus', 'ShippedStatus', 'DeliveredStatus' und 'Delivery'.
"""


class DeliveryStatus:
    pass


class OrderReceivedStatus(DeliveryStatus):
    pass


class ShippedStatus(DeliveryStatus):
    pass


class DeliveredStatus(DeliveryStatus):
    pass


class Delivery:
    pass


if __name__ == "__main__":
    delivery = Delivery()
    delivery.progress_status()
    print(delivery.get_status())  # Output: OrderReceivedStatus
    delivery.progress_status()
    print(delivery.get_status())  # Output: ShippedStatus
    delivery.progress_status()
    print(delivery.get_status())  # Output: DeliveredStatus