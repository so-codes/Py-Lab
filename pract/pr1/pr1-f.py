# Write a recursive function to print the factorial for a given number.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a number: "))

print("Factorial of ", number , "is 1 ") if number == 0 or number == 1 else print(factorial(number))

sum = 1
i = 1
num = int(input("enter number: "))

while i <= num:
    sum = sum * i
    i += 1

print(sum)