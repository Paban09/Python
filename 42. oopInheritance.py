#single Inheritance

class Employee:
    company="Google"
    def __init__(self):
        print("Employee object created")

    def showDetails(self):
        print("Employee works for payment")


class Programmer(Employee):
    language="Python"

    def __init__(self):
        print("Prorammer object created")

    def getLanguage(self):
        print(f"Language he knows is {self.language}")

    def getCompany(self):
        print(f"Company he works for is {self.company}")

    #overriding
    def showDetails(self):
        print("This showDetails is form programmer")


pabon=Employee()
pabon.showDetails()

ayan=Programmer()
ayan.getLanguage()
ayan.showDetails()

print(ayan.company)

ayan.getCompany()
