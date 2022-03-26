#example 1
course='Python For Beginners'
print(course[0])
print(course[0:3])
print(course[:])

#example 2
another=course[:]
print(another)

#example 3
first=input('First: ')
last=input('Last: ')
msg=f'{first} [{last}] is a coder'
print(first+' ' + last+' ' + 'is a coder')
print(msg)


