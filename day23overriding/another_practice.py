#practice

class person:
    def role(self):
        print("person")

class student(person):
    def role(self):
        print("student")
p = person()
p.role()
s = student()
s.role()        
