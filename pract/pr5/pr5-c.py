# Write a Python program to sum all the items in a dictionary

dict = {
    'a': 1, 
    'b': 2, 
    'c': 3,
    'd': 4,
    'e': 5,
}

def sum_dict(dict):
    sum = 0
    for key, value in dict.items():
        sum += value
    return sum

print(sum_dict(dict))