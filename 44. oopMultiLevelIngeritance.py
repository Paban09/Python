class Person:
    country="Bangladesh"

    def takeBreak(self):
        print("Take some rest")


class Employee(Person):
    company="Honda"
    def salary(self):
        print(f"Salary is {self.salary}") 

    def takeBreak(self):
        print("I am a employee so i am taking a rest")

class Programmer(Employee):
    company="Fiver"

    def getSalary(self):
        print("No salary to programmers")


p=Person()
p.takeBreak()
e=Employee()
pr=Programmer()
pr.takeBreak()
print(pr.country)