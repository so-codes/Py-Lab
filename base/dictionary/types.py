car = {"brand": "Ford","model": "Mustang","year": 1964}

x = car.keys()
print(x) #before the change

car["color"] = "white"
print(x) #after the change

y = car.values()
print(y)

## Update
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

print("Enter a key: ")
key = input()

print("Enter a value: ")
value = input()

thisdict.update({key: value})
print(thisdict)