# Write a Python program to read an entire text file

def read_file(filename):
    txt = open(filename, 'r')
    print(txt.read())

read_file('/home/criz/Documents/GitHub/Py-Lab/pract/pr6/pog.txt')