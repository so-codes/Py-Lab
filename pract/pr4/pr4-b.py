# Write a Python program to print a specified list after removing the 0th, 2nd, 4th and 5th elements

def print_list(list):
    list.pop(0)
    list.pop(2)
    list.pop(4)
    list.pop(5)
    print(list)

print_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])