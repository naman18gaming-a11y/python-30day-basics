class Employee:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

# creating object of a class
emp = Employee('naman', 10000)

# accessing private data members
print('Salary:', emp.__salary)