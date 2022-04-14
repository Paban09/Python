class Employee:
    company="Google"
    def getSalary(self):
        print(f"Salary is {self.salary}")

pabon=Employee()
pabon.salary=100000
pabon.getSalary()