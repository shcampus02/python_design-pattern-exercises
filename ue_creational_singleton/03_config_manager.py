# Goal: Create a ConfigurationManager class that loads configuration settings from a source once and makes these
# settings available throughout the application.

# Explanation: Configuration settings are typically loaded during application startup and must remain consistent
# during runtime. The Singleton pattern ensures that configuration settings are loaded and stored once, preventing
# discrepancies and redundant operations (like I/O reading) throughout the application's lifecycle.







if __name__ == '__main__':
    config1 = ConfigurationManager()
    config2 = ConfigurationManager()
    config1.load({'api_key': '1234'})

    print(config1 == config2)  # Should output: True
    print(config1.get_config())  # Should show loaded configuration from config1 load method
    print(config2.get_config())  # Should show the same configuration as config1
