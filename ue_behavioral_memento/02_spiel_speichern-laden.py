"""
Übung 2 - Spiel Speichern und Laden

Das Memento-Muster kann auch bei der Implementierung von Speichern- und Ladenfunktionen in einem
Videospiel hilfreich sein.

Implementieren Sie die Klassen 'Game', 'GameState' und 'GameCareTaker'.
"""


class Game:
    pass


class GameState:
    pass


class GameCaretaker:
    pass


if __name__ == "__main__":
    game = Game()
    caretaker = GameCaretaker()
    game.play()  # Spieler spielt eine Weile...
    caretaker.save_game(game)  # Speichern des Spielzustands
    game.play()  # Spieler spielt weiter und macht Fortschritte..
    caretaker.load_game(game)  # Spieler lädt das Spiel und kehrt zum gespeicherten Zustand zurück