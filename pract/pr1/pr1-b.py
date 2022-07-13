# Enter the number from the user and depending on whether the number is evenor odd, print out an appropriate message to the user

number = int(input("Enter a number: "))

def num_type(number):
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

num_type(number)
