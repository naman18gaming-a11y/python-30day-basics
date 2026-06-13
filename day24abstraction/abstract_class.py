from abc import ABC, abstractmethod
class animal(ABC):
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        print("woof") 

d= dog()
d.sound()          