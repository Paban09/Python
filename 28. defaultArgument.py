
# When the value doesn't pass by paremeter it will use the default value
def greet(name="Pabon"):
    print(f"Hello {name}")


x=input("Enter your name: ")
greet(x)
greet()