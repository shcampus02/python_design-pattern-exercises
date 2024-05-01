# Create a factory pattern to instantiate various computer accessories,
# like Keyboard and Mouse, where each accessory has a method to connect to the computer.


# Test the functionality of the Accessory Factory
if __name__ == '__main__':
    keyboard = AccessoryFactory.get_accessory("keyboard")
    print("Testing keyboard connection: ", end="")
    keyboard.connect()

    mouse = AccessoryFactory.get_accessory("mouse")
    print("Testing mouse connection: ", end="")
    mouse.connect()
