class Employee:
    company="ACI"
    salary=200
    location="Dhaka"


    # #changing the salary of object instance
    # def changeSalary(self,sal):
    #     self.salary=sal


    # #chanding class value by dunder class
    # def changeSalary(self,sal):
    #     self.__class__.salary=sal

    #chanding class value by decorator
    @classmethod
    def changeSalary(cls,sal):
        cls.salary=sal

e=Employee()
print (e.salary)
e.changeSalary(150)
print (e.salary)
print(Employee.salary)