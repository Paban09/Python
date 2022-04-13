class Employee:
    name="Google"
    budget=3000

company1=Employee()
company2=Employee()

# #creating instance attribute budget for both objects
# company1.budget=5000
# company2.budget=7000


print(company1.name)
print(company2.name)
company2.budget=7000
print(company1.budget)
print(company2.budget)


