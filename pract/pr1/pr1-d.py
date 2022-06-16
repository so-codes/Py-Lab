# Write a function that reverses the user defined value

print("Enter a value: ")
value = input()

def reverse(value):
    return value[::-1]
    
print(reverse(value))