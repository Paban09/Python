myDict={
    "Fast": "In a quick manner",
    "Pabon" : "Is a coder",
    "Marks" : [80,90,66],
    "anotherDict": {
        "Name": "Pabon",
        "Id": "18-36348-1"
    },
    1:2
}

print(myDict.items()) #prints the (keys,values) for all content of the dictionary

print(myDict.keys()) #prints the keys of the dictionary

print(myDict['Pabon']) #this will throgh error if the key is not availabe and to get a value has to use .key method
print(myDict.get('Pabon')) #Print the data of desired index

print(list(myDict.keys())) #Type casting class dict keys into list 

# update use to add or update a content in key value pairs in dictionary
updateDict={
    "Mridul":"Is a doctor"
}
 
myDict.update(updateDict)
print(myDict)

myDict.update({"Talha":"Engineer"})
print(myDict)

myDict.update({"Talha":"Failure"}) #updating a value through a key
print(myDict)
