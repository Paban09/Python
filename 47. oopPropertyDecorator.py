class Employee:
    company="Google"
    salary=200
    salaryBonus=25
    
    @property
    def totalSalary(self):
        return self.salary+self.salaryBonus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salaryBonus=val-self.salary


e=Employee()
print(e.totalSalary)
e.totalSalary=220
print(e.salary)
print(e.salaryBonus)