
class Employee:
    compnay="Google"
    ecode= 12340


class Freelancer:
    company="Fiver"
    level= 0

    def upgradeLevel(self):
        self.level=self.level+1 


class Programmer(Employee,Freelancer):
    name="Pabon"


p=Programmer()
print(p.level)
p.upgradeLevel()
print(p.level)
print(p.company)



