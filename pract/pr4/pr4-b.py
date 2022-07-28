# Write a Python program to print a specified list after removing the 0th, 2nd, 4th and 5th elements

l1 = []
print("Enter 10 elements in the list")

for i in range(10):
    print("Enter element ", i+1, ":", end="")
    element = input()
    l1.append(element)

print("List before removing elements", l1)
l1.pop(5)
l1.pop(4)
l1.pop(2)
l1.pop(0)
print("List after removing elements", l1)