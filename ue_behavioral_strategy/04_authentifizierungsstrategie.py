"""
Übung 4 - Authentifizierungsstrategie

Das Strategy-Muster kann in einem Authentifizierungssystem verwendet werden, um
verschiedene Methoden zur Überprüfung der Benutzeridentität zu ermöglichen.

Implementieren Sie die Klassen 'AuthStrategy', 'BasicAuthStrategy', 'OAuthStrategy' und 'AuthContext'.
"""


class AuthStrategy:
    pass


class BasicAuthStrategy(AuthStrategy):
    pass


class OAuthStrategy(AuthStrategy):
    pass


class AuthContext:
    pass


if __name__ == "__main__":
    context = AuthContext(OAuthStrategy())
    context.authenticate("myUser", "myPwd")
    context.set_strategy(BasicAuthStrategy())
    context.authenticate("myUser", "myPwd")