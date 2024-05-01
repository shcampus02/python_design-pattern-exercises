"""
Übung 4 - Zusätzliche Benutzer-Rollen

In dieser Übung verwenden wir das Decorator-Pattern, um zu definieren, welche Klassen von Benutzern auf welche
Ressourcen im System zugreifen können. Mit dem Decorator-Pattern können wir Flexibilität neue Rollen hinzufügen,
ohne die ursprüngliche Benutzerklasse ändern zu müssen.

Implementieren Sie die Klassen 'User', 'AdminDecorator', 'DeveloperDecorator' und 'ManagerDecorator'.
"""


class UserComponent:
    def has_access(self):
        pass


class User(UserComponent):
    def has_access(self):
        pass


class Decorator(UserComponent):
    def __init__(self, component):
        pass


class AdminDecorator(Decorator):
    def has_access(self):
        pass


class DeveloperDecorator(Decorator):
    def has_access(self):
        pass


class ManagerDecorator(Decorator):
    def has_access(self):
        pass


if __name__ == "__main__":
    user = User()
    admin_user = AdminDecorator(user)
    dev_user = DeveloperDecorator(user)
    manager_user = ManagerDecorator(user)

    users = [admin_user, dev_user, manager_user]
    for user in users:
        print(user.has_access())
