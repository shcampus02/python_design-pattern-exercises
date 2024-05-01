"""
Übung 1 - Chatroom Mediator

Das Mediator-Muster kann sehr nützlich sein bei der Implementierung eines
Chatroom-Dienstes. Jeder Benutzer (oder "Kollege" im Kontext des Mediator-Musters)
sollte in der Lage sein, Nachrichten zu senden, ohne sich um die anderen Benutzer sorgen zu müssen.
Der Mediator kümmert sich um die Verteilung der Nachrichten an alle Benutzer.

Implementieren Sie die Klassen 'ChatMediator', 'User', 'ChatUser' und 'AdminUser'.
"""


class ChatMediator:
    pass


class User:
    pass


class ChatUser:
    pass


class AdminUser:
    pass


if __name__ == "__main__":
    mediator = ChatMediator()
    user1 = ChatUser(mediator, "User 1")
    user2 = AdminUser(mediator, "Admin 1")
    mediator.add_user(user1)
    mediator.add_user(user2)
    user1.send_message("Hello everyone!")  # Message will reach all users through the mediator