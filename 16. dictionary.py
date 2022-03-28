#Collection of key value pairs

myDict={
    "Fast": "In a quick manner",
    "Pabon" : "Is a coder",
    "Marks" : [80,90,66],
    "anotherDict": {
        "Name": "Pabon",
        "Id": "18-36348-1"
    }
}

print(myDict['Marks'])

print(myDict['anotherDict']['Name'])

myDict['Marks']=[45,40,30]
print(myDict['Marks'])