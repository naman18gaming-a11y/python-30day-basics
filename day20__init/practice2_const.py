# class Mobile with constructor
class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_mobile(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


# ✅ Create objects
phone1 = Mobile("Apple", 50000)
phone2 = Mobile("Samsung", 56000)

# Call method
phone1.show_mobile()
phone2.show_mobile()
