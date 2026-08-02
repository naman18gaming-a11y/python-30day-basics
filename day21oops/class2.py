class Student:
    school_name = "Public School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Student:", self.name, "Age:", self.age, "School:", Student.school_name)

    def change_age(self, age):
        self.age = age

    @classmethod
    def modify_school_name(cls, new_name):
        cls.school_name = new_name



s1 = Student("Naman", 20)
s1.show()


s1.change_age(21)
s1.show()

# Modify school name
Student.modify_school_name("International School")
s1.show()
