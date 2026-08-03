#Exercise 4: Student Class with Average Grade
class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.average = sum(self.marks) / len(self.marks)

    def __init__(self):
        print('name:', 'name','marks:', 'marks')

s1=student('naman',50)    
s2 = student('cnaman',20)  