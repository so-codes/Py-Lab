thisdict = {}
r1 = int(input("Enter a range: "))
for i in range(r1):

    key = input("Enter a key: ")
    value = input("Enter a value: ")

    thisdict.update({key: value})

print(thisdict)