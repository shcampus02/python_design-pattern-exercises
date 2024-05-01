# Design a Configuration class that can clone system configurations and
# allows modifying individual settings without affecting other instances.




if __name__ == '__main__':
    config = Configuration()
    config.set_property("resolution", "1920x1080")
    config.set_property("volume", "100")

    cloned_config = config.clone()
    cloned_config.set_property("volume", "70")
    print(config)        # resolution: 1920x1080, volume: 100
    print(cloned_config) # resolution: 1920x1080, volume: 70
