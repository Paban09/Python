greeting="Good morning, "
name="Pabon"

print(greeting+name) #string concatanation
c= greeting+name
print(c)
print(name[0])

if name[0:2]=='Pa':
   print("True")
else:
   print("False")

print(name[-3:-1])

print(name[0:len(name):2]) #slicing with skip value