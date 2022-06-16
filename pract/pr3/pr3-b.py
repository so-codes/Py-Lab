# write a program that prints out all the elements of the list that are less than 5

a=[1,1,2,3,5,8,13,21,34,55,89]

def less_than_5(list):
    for i in list:
        if i < 5:
            print(i)

less_than_5(a)