"""
Übung 1 - Authentifizierungskette

In dieser Übung sollen Sie eine Kette der Verantwortung für die Authentifizierung implementieren. Die Kette sollte
aus mehreren Authentifizierungsschritten bestehen, z.B. Nutzernamen-Prüfung, Passwort-Prüfung und 2-Faktor Authentifizierung.
Jeder Schritt sollte ein Glied in der Kette der Verantwortung sein.

Implementieren Sie die Klassen UserCheckHandler, PasswordCheckHandler und TwoFactorAuthHandler, jede davon ein Glied der Chain of Responsibility.
"""


class AbstractHandler:
    # Platz für Ihre Implementierung
    pass


class UserCheckHandler(AbstractHandler):
    # Platz für Ihre Implementierung
    pass


class PasswordCheckHandler(AbstractHandler):
    # Platz für Ihre Implementierung
    pass


class TwoFactorAuthHandler(AbstractHandler):
    # Platz für Ihre Implementierung
    pass


if __name__ == "__main__":
    # Hier sind einige vordefinierte Tests. Erweitern Sie Ihre Implementierung so, dass sie diese Tests bestehen.
    auth_chain = UserCheckHandler(PasswordCheckHandler(TwoFactorAuthHandler()))

    # Test 1
    assert auth_chain.handle(("admin", "adminpassword", "123456")) == "User authenticated"
    # Test 2
    assert auth_chain.handle(("admin", "wrongpassword", "123456")) == "Invalid password"
    # Test 3
    assert auth_chain.handle(("unknown", "adminpassword", "123456")) == "User not found"
