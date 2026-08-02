#practice:
class comapny:
    def __init__(self, name, dep, age):
        self.name = name
        self.dep = dep
        self.age = age

    def show(self):
        print('name:', self.name, 'department:', self.dep, 'Age:', self.age)


s1 = comapny('naman', 'IT', 55)
s1.show()
