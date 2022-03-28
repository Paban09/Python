from ast import operator


a=3
b=4

print("Sumation of a,b= ",a+b)
print("Subtruction of a,b= ",a-b)
print("Mutiply of a,b= ",a*b)
print("Division of a,b= ",a/b)
print("Expodential of a,b= ",a**b)

#assignment operators

c=34
c +=1
print(c)

#comperison operators

d=(a>b)
print(d)

# logical operator

bool1=True
bool2=False

print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The value of not bool2 is", (not bool2))