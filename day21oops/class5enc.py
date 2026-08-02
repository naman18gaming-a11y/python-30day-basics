#Information Hiding and conditional logic for setting an object attributes
class students:
    def __init__(self,name,roll_no,age):
        self.name = name
        self.__roll_no = roll_no
        self.__age = age

        def show(self):
            print('name:', self.name, 'roll_no:', self.__roll_no, 'age:', self.__age)
        def set_roll_no(self,roll_no):
            if roll_no > 0:
                self.__roll_no = roll_no
            else:
                print('roll_no should be greater than 0')    
naman = students('naman', 1, 20)
naman.show()
naman.set_roll_no(121)
naman.show()