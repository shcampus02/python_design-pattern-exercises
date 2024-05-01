"""
Übung 2 - Mediator für Komponenten

Das Mediator-Muster kann auch nützlich sein für die Kommunikation zwischen verschiedenen
Komponenten einer Anwendung. Wenn zum Beispiel ein Klick auf einen Button eine Änderung in
einigen anderen Komponenten verursachen soll, könnte ein Mediator diese Verbindung herstellen.

Implementieren Sie die Klassen 'ComponentMediator', 'Component', 'ButtonComponent' und 'TextComponent'.
"""


class ComponentMediator:
    pass


class Component:
    pass


class ButtonComponent:
    pass


class TextComponent:
    pass


if __name__ == "__main__":
    mediator = ComponentMediator()
    button = ButtonComponent(mediator, "Button")
    text = TextComponent(mediator, "Text")
    mediator.add_component(button)
    mediator.add_component(text)
    button.click()  # This will trigger some changes in TextComponent through the mediator