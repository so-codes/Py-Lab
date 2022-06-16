# Define a function that computes the length of a given list or string.

def length(v):
    print("The length of", v, "is", len(v))
    return len(v)

print("Enter a list or string: ")
value = input()

length(value)