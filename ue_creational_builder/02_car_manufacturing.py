# Design a CarBuilder class to simulate the construction of a car with different components
# # such as engine, tires, and seats.
# # This exercise will help you understand how to manage complex objects with multiple parts.



if __name__ == '__main__':
    car_builder = CarBuilder()
    car = car_builder.add_engine("V8 Engine")\
                     .add_tires("All-season tires", 4)\
                     .add_seats("Leather seats", 5)\
                     .build()
    print(car)
