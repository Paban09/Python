x=input("How is the weather: ")

if((x.find("hot"))>=0 and (x.find("raining"))>=0):
    print("Drink more water and take umbrella when go to outside.")
elif((x.find("hot"))>=0 or (x.find("cloudy"))>=0):
    print("Drink more water.")
elif((x.find("cold"))>=0):
    print("Wear warm cloths")
elif not ((x.find("raining"))>=0):
    print("Enjoy the day")

