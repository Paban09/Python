def avg(mark):
    x=sum(mark) / len(mark)
    return x


number=[5,6]
marks=[]
sub=int(input("How many Subjects: "))

for i in range(1,sub+1):
    x=int(input(f"Input Mark of the Subject {i}: "))
    marks.insert(i,x)

print("The list of the mark is: ",marks)

avarage=avg(marks)
avg2=avg(number)
print("The avarage of the mark is: ",avarage)
print("The avarage of the number is: ",avg2)