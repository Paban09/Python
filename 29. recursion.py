from re import X


def factorial(x):
    if (x==0 or x==1):
        return x
    else:
        x=x*factorial(x-1)
        return x

i=int(input("Input a no: "))

print(factorial(i))