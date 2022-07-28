# Write a Python program to clone or copy a list

l1 = []
for i in range(5):
    print("Enter element", i + 1, ":", end="")
    element = input()
    l1.append(element)

print("Original list: ", l1)


def copy_list(l1):
    l2 = l1.copy()
    l1.append(10)
    print("Original list after append: ", l1)
    print("Copied list: ", l2)


copy_list(l1)
