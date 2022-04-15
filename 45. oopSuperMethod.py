class Person:
    country="Bangladesh"

    def __init__(self):
        print("Initailizing Person \n")

    def takeBreak(self):
        print("Take some rest")


class Employee(Person):
    company="Honda"

    def __init__(self):
        super().__init__()
        print("Initailizing Employee")


    def salary(self):
        print(f"Salary is {self.salary}") 

    def takeBreak(self):
        print("I am a employee so i am taking a rest")

class Programmer(Employee):
    company="Fiver"

    def __init__(self):
        super().__init__()
        print("Initailizing Programmer")

    def getSalary(self):
        print("No salary to programmers")

    def takeBreak(self):
        super().takeBreak()
        print("I am a programmer so i am taking a rest")


# p=Person()

pr=Programmer()

# p.takeBreak()
# pr.takeBreak()
# print(pr.country)


# e=Employee()