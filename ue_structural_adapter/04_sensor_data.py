# Develop an adapter that normalizes data from various types of sensors (e.g., temperature, humidity, light)
# so they can be processed in a uniform manner by an analytics system.

# In systems that gather data from various sensors, each type of sensor might output data in different formats or
# units. An adapter can standardize this data into a consistent format for the analytics systems, simplifying the
# data processing pipeline and ensuring that the core system can interpret any sensor data uniformly.








if __name__ == '__main__':
    sensor_system = SensorSystem()
    temperature_sensor = TemperatureSensor()
    humidity_sensor = HumiditySensor()

    temperature_adapter = SensorAdapter(temperature_sensor, "Celsius")
    humidity_adapter = SensorAdapter(humidity_sensor, "Percent")

    # Normalizing and reading sensor data
    print("Temperature:", temperature_adapter.read_sensor())
    print("Humidity:", humidity_adapter.read_sensor())
