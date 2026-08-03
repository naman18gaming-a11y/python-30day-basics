#Exercise 3: Rectangle Class with Area & Perimeter
class rectangle:
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width
        self.perimeter = 2 * (lenght + width)
        self.area = lenght * width

    def show(self):  
        print('Area:', self.area, 'Perimeter:', self.perimeter)  

r1 = rectangle(2,5)        
r1.show()