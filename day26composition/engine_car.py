# engine_car.py

class Engine:
    def start(self):
        print("Engine started!")


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()   # Car contains Engine

    def drive(self):
        # Use Engine's start method
        self.engine.start()
        print(f"{self.brand} car is now driving...")



c1 = Car("Toyota")
c1.drive()
