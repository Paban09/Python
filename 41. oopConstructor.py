class Employee:
    company="Google"

    # def __init__(self):
    #     print("Employee is Created")

    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print(f"Employee name is {name} and slary is {salary}. \nWork for {subunit} which company is {self.company}")

    def getDetails(self):
        print(f"Employee name is {self.name}") 
        print(f"Employee salary is {self.salary}") 
        print(f"Employee compnay is {self.company}") 
        print(f"Employee subunit is {self.subunit}") 



    def getSalary(self):
        print(f"Employee Salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning, sir. ")


pabon=Employee("Paban",500,"YouTube")
pabon.getDetails()
# pabon1.salary=100000

# pabon1.getSalary()
# pabon1.greet()