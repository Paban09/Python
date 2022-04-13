class Employee:
    name="Google"


company1=Employee()
company2=Employee()

print(company1.name)
print(company2.name)

Employee.name="Microsoft"

print(company1.name)
print(company2.name)


