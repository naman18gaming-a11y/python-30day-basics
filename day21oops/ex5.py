#Exercise 5: Product Class with Stock Value Calculator
class product:
    def __init__(self,name,quantity,price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def total_value(self):
        return self.price * self.quantity

p1 = product('lappy',500,10000)
print(f"Total stock value of {p1.name}: ${p1.total_value():.2f}")
        