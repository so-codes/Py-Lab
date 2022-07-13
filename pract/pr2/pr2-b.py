# Define a function that computes the length of a given list or string.

def length(v):
    print("The length of", v, "is", len(v))
    return len(v)

value = input("Enter a list or string: ")

length(value)