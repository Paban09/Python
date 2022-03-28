x=input("How is the weather: ")

if(x.find("hot"))>=0:
    print("Drink water")
elif(x.find("cold"))>=0:
    print("Wear warm cloths")
else:
    print("Enjoy the day")