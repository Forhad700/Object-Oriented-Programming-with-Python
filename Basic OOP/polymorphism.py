class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def sound(self):
        return "Barks!"
    
class Cat(Animal):
    def sound(self):
        return "Meow!"
    
def animal_sound(animal):
    return animal.sound()

dog = Dog("Tommy")
cat = Cat("Luna")

print(dog.name, animal_sound(dog))
print(cat.name, animal_sound(cat))