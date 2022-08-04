# Write a Python program to sum all the items in a dictionary

oi = print

dict1 = dict()
no = int(input("How many key values do u wish to have: "))

for i in range(no):
    data = input("Enter key & value for dict1 :")
    temp = data.split(":")
    dict1[temp[0]] = int(temp[1])

def sum_dict(di):
    sum_di = 0
    for key, value in di.items():
        sum_di += value
    return 'Sum of dict is :', sum_di

oi(sum_dict(dict1))