"""
Übung 4 - Interaktive WebUI-Benutzerkomponenten

In dieser Übung nutzen wir das Flyweight-Pattern, um verschiedene wiederverwendbare Benutzerkomponenten in einem Web-User-Interface zu implementieren.
Mit dem Flyweight-Pattern können wir mehrere Instanzen einer bestimmten Benutzerkomponente erstellen, ohne viel Speicherplatz zu verbrauchen.

Implementieren Sie die Klassen 'WebUIComponent' und 'WebUIComponentFactory'.
"""


class WebUIComponent:
    pass


class WebUIComponentFactory:
    pass


if __name__ == "__main__":
    factory = WebUIComponentFactory()
    component1 = factory.get_web_ui_component('Button')
    component2 = factory.get_web_ui_component('CheckBox')
    component3 = factory.get_web_ui_component('Button')
    print(id(component1), id(component2), id(component3))  # Die Ids von component1 und component3 sollten gleich sein.
