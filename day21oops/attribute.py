#creating data using private attribute and getter:

class student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def get_student(self):
        print("NAME:", self.__name)
        print("marks", self.__marks)

student1 = student("naman", 99)
student2 = student("twisha", 91)

student1.get_student()
student2.get_student()