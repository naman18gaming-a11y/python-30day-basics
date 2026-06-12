# create a prent child inhertance
class animal:
    def show(self):
        print("eat")

class dog(animal):
    def bark(self):
        print("woof")
d = dog()
 
d.show()
d.bark()
