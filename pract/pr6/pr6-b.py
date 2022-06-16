# Write a Python program to read last n lines of a file

def read_last_lines(filename, n):
    with open(filename, 'r') as f:
        lines = f.readlines()
        print(lines[-n:])

read_last_lines('/home/criz/Documents/GitHub/Py-Lab/pract/pr6/pog.txt', 1)