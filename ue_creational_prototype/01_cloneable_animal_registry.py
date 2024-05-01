# Create an Animal class with cloning capabilities that also tracks the habitat preference.
# The registry should clone animals and modify their habitat without affecting the original.




if __name__ == '__main__':
    animal_registry = AnimalRegistry()
    tiger = animal_registry.register_animal("Tiger", "Forest")
    print(tiger)  # Tiger, Habitat: Forest

    cloned_tiger = tiger.clone()
    cloned_tiger.set_habitat("Mountain")
    print(tiger)      # Tiger, Habitat: Forest
    print(cloned_tiger)  # Tiger, Habitat: Mountain
