class SingletonMeta(type):
    _instances = {}
 
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
 
class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value
 
singleton1 = Singleton("First Instance")
singleton2 = Singleton("Second Instance")
 
print(singleton1.value)  
print(singleton2.value)