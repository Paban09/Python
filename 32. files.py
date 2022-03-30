# f=open('32. sample.txt','r') #opening a file
f=open('32. sample.txt') #by deafault the mode is 'r'
data=f.read() #reading a file
print(data)
f.close() #closing a file