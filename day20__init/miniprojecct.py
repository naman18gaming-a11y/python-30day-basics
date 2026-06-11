#mini project emplooye mangment 
class employe:
    def __init__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def show_employe(self):
        print("NAME:", self.name)
        print("SALARY:",self.salary)
        print("DEPARTMENT:",self.department)

# create instances outside the class
employe1 = employe("NAMAN", 30, "it")
employe2 = employe("TWISHA", 100, "air")

# call the method
employe1.show_employe()
employe2.show_employe()


