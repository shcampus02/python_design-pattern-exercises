"""
Übung 3 - Wetterstation

In einem Wetterstationsystem können Wetteranzeigen das Observer-Muster verwenden,
um Updates über Wetteränderungen zu erhalten.

Implementieren Sie die Klassen 'WeatherData', 'WeatherDisplay' und 'WeatherStation'.
"""


class WeatherData:
    pass


class WeatherDisplay:
    pass


class WeatherStation:
    pass


if __name__ == "__main__":
    station = WeatherStation()
    display = WeatherDisplay()
    station.register(display)
    station.change_weather("Sunny", 25)
    display.update()