class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def sound(self):
        return "Barks!"
    
class Cat(Animal):
    def sound(self):
        return "Meow!"
    
dog_instance = Dog("Tommy")
cat_instance = Cat("Luna")

print(dog_instance.name, dog_instance.sound())
print(cat_instance.name, cat_instance.sound())