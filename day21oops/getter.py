# Employee class with private attributes and getter
class Employee:
    def __init__(self, name, salary):
        self.__name = name        # private attribute
        self.__salary = salary    # private attribute

    
    def get_salary(self):
        return self.__salary

    
    def get_name(self):
        return self.__name



emp1 = Employee("Naman", 50000)
emp2 = Employee("Twisha", 70000)

# Access private attributes using getter
print("Name:", emp1.get_name(), "| Salary:", emp1.get_salary())
print("Name:", emp2.get_name(), "| Salary:", emp2.get_salary())
