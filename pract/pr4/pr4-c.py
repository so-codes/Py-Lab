# Write a Python program to clone or copy a list

def clone_list(list):
    return list[:]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("cloned list: ", clone_list(list))

list.append(11)  # appended to the original list just to confirm the copy
print("original list: ", list)
