"""
Übung 1 - Newsletter System

Das Observer-Muster kann nützlich sein, um ein Newsletter-System zu implementieren.
Ein User kann sich für einen Newsletter-Anbieter anmelden und erhält dann Updates,
wann immer dieser Anbieter einen neuen Newsletter veröffentlicht.

Implementieren Sie die Klassen 'Newsletter', 'User' und 'NewsletterProvider'.
"""


class Newsletter:
    pass


class User:
    pass


class NewsletterProvider:
    pass


if __name__ == "__main__":
    provider = NewsletterProvider()
    user = User()
    provider.register(user)
    provider.publish_newsletter("This is our new newsletter!")
    user.update()