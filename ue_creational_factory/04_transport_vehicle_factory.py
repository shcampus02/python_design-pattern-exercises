# Implement a factory pattern to create different types of transport vehicles,
# such as Car and Truck, where each vehicle has a method to describe its movement.




# Test the functionality of the Vehicle Factory

if __name__ == '__main__':
    car = VehicleFactory.get_vehicle("car")
    print("Testing car movement: ", end="")
    car.move()

    truck = VehicleFactory.get_vehicle("truck")
    print("Testing truck movement: ", end="")
    truck.move()
