#class car using oops
class car:
    def __init__(self,brand,modle,year):
        self.brand = brand
        self.modle = modle
        self.year = year

    def display_info(self):
        print("-----DISPLAY CAR INFORMATION")
        print("car brand:", self.brand)    
        print("car modle:", self.modle)
        print("car year:",self.year)



car1 = car("toyota", "camary", 2021)
car2 = car("toyota", "hilux", 2023)
car3 = car("toyota", "land crusiser", 2025)

car1.display_info()
car2.display_info()
car3.display_info()
