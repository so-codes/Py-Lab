# Define a procedurehistogram() that takes a list of integers and prints a histogram to the screen.

def histogram(list):
    print("")
    for i in list:
        print(i * "*")
    
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

histogram([num1, num2, num3])
