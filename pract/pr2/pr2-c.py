# Define a procedurehistogram() that takes a list of integers and prints a histogram to the screen.

def histogram(list):
    print("")
    for i in list:
        print(i * "*")
    
print("Enter num 1: ")
num1 = int(input())

print("Enter num 2: ")
num2 = int(input())

print("Enter num 3: ")
num3 = int(input())

histogram([num1, num2, num3])
