# Input user name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old
print("Enter your name: ")
name = input()
print("Enter your age: ")
age = int(input())
print("")
print("Hello " + name + ", you will turn 100 years old in the year " + str(2022 + (100 - age)))