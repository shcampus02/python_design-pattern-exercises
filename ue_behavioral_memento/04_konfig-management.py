"""
Übung 4 - Konfigurationsmanagement

Die Memento-Entwurfsmusters kann hilfreich sein, um Konfigurationseinstellungen zu speichern und wiederherzustellen.

Implementieren Sie die Klassen 'Config', 'ConfigSnapshot' und 'ConfigManager'.
"""


class Config:
    pass


class ConfigSnapshot:
    pass


class ConfigManager:
    pass


if __name__ == "__main__":
    manager = ConfigManager()
    config = Config()
    config.set("light_mode", True)
    manager.make_snapshot(config)
    config.set("light_mode", False)
    manager.restore(config)
    print(config.get("light_mode"))  # Output: True