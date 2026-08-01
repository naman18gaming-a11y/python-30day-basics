#jessa = Person('Jessa', 'Female', 'Software Engineer
class Person:
    def __init__(self, name, sex, profession):
        self.name = name
        self.sex = sex
        self.profession = profession

    def show(self):
        print("Name:", self.name)
        print("Sex:", self.sex)
        print("Profession:", self.profession)

    def work(self):
        print(self.name, "is working as a", self.profession)



naman = Person("Naman", "Male", "ML Engineer")

naman.show()
naman.work()
