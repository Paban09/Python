class Employee:
    company="Google"
    def getSalary(self):
        print(f"Salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning, sir. ")

pabon=Employee()
pabon.salary=100000
# pabon.getSalary()

pabon.greet()