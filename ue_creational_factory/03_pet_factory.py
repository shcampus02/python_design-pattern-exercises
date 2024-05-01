#Create a factory method to instantiate different types of pets (e.g., Dog, Cat).
# Each pet type should have a method to make a sound (e.g., bark, meow).





# Test the functionality of the Pet Factory
if __name__ == '__main__':
    dog = PetFactory.get_pet("dog")
    print("Dog says: ", end="")
    dog.make_sound()

    cat = PetFactory.get_pet("cat")
    print("Cat says: ", end="")
    cat.make_sound()
