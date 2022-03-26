numbers=[5,2,1,5,7,2,4]
x=numbers[0]
for y in numbers:
    if x!=y:
        x=y
    else:
        numbers.remove(x)

print(numbers)
