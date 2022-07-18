# Define a function that computes the length of a given list or string.

def lengthStr(v):
    return len(v)

def lengthList(b):
    return len(b)

value = input("Enter a string: ")
print("The length of string", lengthStr(value))

l1 = [10, "pog", 39.23]
print("The length of list is: ", lengthList(l1))