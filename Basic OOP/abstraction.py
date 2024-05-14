from abc import ABC, abstractmethod
class AbstractDemo(ABC):                        # Abstract Class
    @abstractmethod                            # Abstract Method
    def display(self):
        None

    @abstractmethod                            # Abstract Method
    def show(self):
        None

class Demo1(AbstractDemo):                     # Abstract Class
    def display(self):
        print("Abstract Method")

class Demo2(AbstractDemo):                     # Concrete Class
    def display(self):
        print("Display Method")
    def show(self):
        print("Show Method")


d2 = Demo2()
d2.display()
d2.show()