b=set()

#adding value in set
b.add(1)
b.add(5)
b.add(6)
b.add(9)
b.add(9) #adding a value repetatively doesn't change the set
b.add((1,2,3,4)) #can inpyt tuple in set
print(b)

print("Print the length of the set: ",len(b))
b.remove(1)
print(b)