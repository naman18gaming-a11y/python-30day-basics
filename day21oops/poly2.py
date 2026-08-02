#Multiple Inheritance
class person:
    def person_info(self,name,age):
        print('Inside person class')
        print('Name:', name, 'Age:', age)

class company:
    def company_info(self,company_name):
        print('Inside company class')
        print('Company Name:', company_name)


class employee(person,company):                
    def employee_info(self, salary):
        print('Inside employee class')
        print('Salary:', salary)
            