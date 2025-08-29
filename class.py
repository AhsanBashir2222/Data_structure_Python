class Dog:
    species = "Caniene"

    def __init__(self, name, age):
        self.name = name
        self.age = age


dog1 = Dog("Buddy", 3)
dog2 = Dog("New", 2)
print(dog1.name, dog1.age, dog1.species)
print(dog2.age, dog2.species, dog2.species)
print(dog1.species)
dog1.species = "Max"
print(dog1.species)
# Single inheritance
