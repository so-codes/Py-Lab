# Input user name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\nHello " + name + ", you will turn 100 years old in the year " + str(2022 + (100 - age)))