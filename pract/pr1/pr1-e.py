# Write a function to check the input value is Armstrong and also write the function for Palindrome.

number = int(input("Enter a number: "))

def isArmstrong():
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if number == sum:
        print("The number is Armstrong")
    else:
        print("The number is not Armstrong")

isArmstrong()

def isPalindrome():
    if str(number) == str(number)[::-1]:
        print("The number is Palindrome")
    else:
        print("The number is not Palindrome")

isPalindrome()

def pali():
    sum = 0 
    temp = number
    while temp > 0:
        digit = temp % 10
        sum = sum * 10 + digit
        temp //= 10
    if number == sum:
        print("The number is Palindrome")
    else:
        print("The number is not Palindrome")

pali()