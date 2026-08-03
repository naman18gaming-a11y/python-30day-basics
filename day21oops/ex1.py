#Exercise 2: Vehicle Class with Instance Attributes
class vech:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def show_info(self):
        print(f'Max Speed: {self.max_speed}, Mileage: {self.mileage}')
c1 = vech(200, 15)
c1.show_info()