# Write a recursive function to print the factorial for a given number.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a number: "))

if number < 0:
    print("Please enter a positive integer")
elif number == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", number, "is:", factorial(number))
