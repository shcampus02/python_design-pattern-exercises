"""
Übung 4 - Mediator für Sensoren

In einem System, das verschiedene Sensoren steuert, kann das Mediator-Muster nützlich sein,
um die Kommunikation zwischen den einzelnen Sensoren zu koordinieren. Der Mediator stellt sicher,
dass Sensoren zusammenarbeiten und sich wechselseitig auf Änderungen reagieren können.

Implementieren Sie die Klassen 'SensorMediator', 'Sensor' und 'TemperatureSensor'.
"""


class SensorMediator:
    pass


class Sensor:
    pass


class TemperatureSensor:
    pass


if __name__ == "__main__":
    mediator = SensorMediator()
    sensor1 = TemperatureSensor(mediator, "Sensor 1")
    sensor2 = TemperatureSensor(mediator, "Sensor 2")
    mediator.add_sensor(sensor1)
    mediator.add_sensor(sensor2)
    sensor1.change_temperature(25)  # This will trigger an update in Sensor2 through the SensorMediator