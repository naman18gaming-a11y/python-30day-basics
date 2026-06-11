# class Car with constructor
class Car:
    def __init__(self, brand):
        self.brand = brand   # instance attribute

    def show_brand(self):
        print(self.brand)


# ✅ Create object
car1 = Car("Toyota")

# Call method
car1.show_brand()
