# create a prent child inhertance
class vehicle:
    def show(self):
        print("cars")

class car(vehicle):
    pass

c = car()
c.show()