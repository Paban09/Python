class RailwayForm:
    formType="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train name is {self.train}")

 
pabonApplication=RailwayForm() #creating the instance of a class
pabonApplication.name="Pabon"
pabonApplication.train="Dhaka Express"

pabonApplication.printData() #calling ta function fromm the class