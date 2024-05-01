"""
Übung 3 - Home-Automation-System

In diesem Fall können Sie den Command Pattern verwenden, um verschiedene Geräte in einem Home-Automation-System zu steuern. Sie könnten zum Beispiel Lichter ein- und ausschalten oder die Thermostateinstellung ändern.

Implementieren Sie die Klassen 'HomeAutomationSystem', 'Command', 'LichtAnCommand', 'LichtAusCommand', 'ThermostatHochCommand', 'ThermostatRunterCommand', 'Licht', 'Thermostat'.
"""


class HomeAutomationSystem:
    pass


class Command:
    pass


class LichtAnCommand:
    pass


class LichtAusCommand:
    pass


class ThermostatHochCommand:
    pass


class ThermostatRunterCommand:
    pass


class Licht:
    pass


class Thermostat:
    pass


if __name__ == "__main__":
    licht = Licht()
    thermostat = Thermostat()
    licht_an_command = LichtAnCommand(licht)
    thermostat_hoch_command = ThermostatHochCommand(thermostat)
    home_automation = HomeAutomationSystem()
    home_automation.set_command(licht_an_command)
    home_automation.button_press()
    home_automation.set_command(thermostat_hoch_command)
    home_automation.button_press()