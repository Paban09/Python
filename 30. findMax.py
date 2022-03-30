def max(num1,num2,num3):
    if(num1>num2)and(num1>num3):
        return num1
    elif (num2>num3):
        return num2
    else:
        return num3
       
x=max(59,55,79)
print(f"the max number is {x}")