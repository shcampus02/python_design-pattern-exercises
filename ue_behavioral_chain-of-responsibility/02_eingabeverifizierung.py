"""
Übung 2 - Eingabeverifizierung

In dieser Übung sollen Sie eine Kette der Verantwortung erstellen, die Benutzereingaben validiert.
Sie könnten unterschiedliche Validatoren für verschiedene Aspekte der Eingabe erstellen, z.B. die Prüfung auf leere Felder,
die Validierung von Email-Adressen oder Telefonnummern.

Implementieren Sie die Klassen EmailValidator, PhoneNumberValidator und EmptyFieldValidator, jede davon als Glied der Chain of Responsibility.
"""


class AbstractValidator:
    # Platz für Ihre Implementierung
    pass


class EmailValidator(AbstractValidator):
    # Platz für Ihre Implementierung
    pass


class PhoneNumberValidator(AbstractValidator):
    # Platz für Ihre Implementierung
    pass


class EmptyFieldValidator(AbstractValidator):
    # Platz für Ihre Implementierung
    pass


if __name__ == "__main__":
    # Hier sind einige vordefinierte Tests. Erweitern Sie Ihre Implementierung so, dass sie diese Tests bestehen.
    validation_chain = EmailValidator(PhoneNumberValidator(EmptyFieldValidator()))

    # Test 1
    assert validation_chain.handle("test@example.com") == "Email is valid"
    # Test 2
    assert validation_chain.handle("invalid_email") == "Invalid email address"
    # Test 3
    assert validation_chain.handle("1234567890") == "Phone number is valid"
    # Test 4
    assert validation_chain.handle("123") == "Invalid phone number"
    # Test 5
    assert validation_chain.handle("") == "Field is empty"
