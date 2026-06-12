#create the overide 

class animals:
    def sound(self):
        print("animal sound")
         
class dog(animals):
    def sound(self):
        print("woof")         

d = dog()
d.sound()