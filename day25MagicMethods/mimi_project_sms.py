#Student Management System (Magic Methods Edition)
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def __str__(self):
        return f"Student: {self.name} | Marks: {self.marks}"  
    
s1 = student("naman",9)     
print(s1)   