letter='''Dear <name>,
Happy Ramadan Mubarak. Wish you all the very  best.

Date= <date>
'''
name=input("Enter name: ")
date=input("Enter date :")

letter= letter.replace('<name>',name)
letter= letter.replace('<date>',date)

print("\n")
print(letter)

print(letter.find('  ')) #finding double space in a string
print(letter.replace('  ',' ')) #replacing double space in a string
