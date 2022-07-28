# Write a program that takes two lists and returns True if they have at least one common member.

no1 = int(input("Enter number of elements in the list: "))

l1 = []
print("Enter ", no1, " elements in the l1")

for i in range(no1):
    print("Enter element ", i + 1, ":", end="")
    element = input()
    l1.append(element)

print(l1)

no2 = int(input("Enter number of elements in the list: "))

l2 = []
print("Enter ", no2, " elements in the l2")

for j in range(no2):
    print("Enter element ", j + 1, ":", end="")
    element = input()
    l2.append(element)

print(l2)


def common_el(list1, list2):
    if len(list1) < len(list2):
        arg1 = list1
        arg2 = list2
    else:
        arg1 = list2
        arg2 = list1

    for z in arg1:
        if z in arg2:
            return True
    return False


if common_el(l1, l2):
    print("Element exists")
else:
    print("element doesnt exist")