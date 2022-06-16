# Write a program that takes two lists and returns True if they have at least one common member.

def common_member(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False

print(common_member([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
print(common_member([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))