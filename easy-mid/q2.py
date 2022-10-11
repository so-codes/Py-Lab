# Develop a Python Program accept value in dictionary and to delete a value from dictionary. 

name = input("Enter name: ")
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
d = {
    "name": name,
    "age": age,
    "marks": marks
}
print(d)

# Delete a value from dictionary
del d["marks"]
print("Dictionary after deleting it is: ", d)