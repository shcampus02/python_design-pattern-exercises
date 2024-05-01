# Goal: Develop a RuntimeSettings class that stores and provides access to runtime settings or configurations that
# need to be accessed and possibly modified by various components of an application.
#
# Explanation: Runtime settings like debug levels or environment details (development, production) are typically set
# at startup and need to be consistently accessible throughout an application's operation. Using the Singleton
# pattern ensures that these settings are stored in a single, globally accessible location, providing coherence and
# ease of management.






if __name__ == '__main__':
    settings1 = RuntimeSettings()
    settings2 = RuntimeSettings()
    settings1.update_setting("debug_level", "high")
    settings2.update_setting("environment", "production")

    print(settings1 == settings2)  # Should output: True
    print(settings1.get_setting("debug_level"))  # Should output: "high"
    print(settings2.get_setting("environment"))  # Should output: "production"
    print(settings1.get_all_settings())  # Should show all settings including those set via settings2
