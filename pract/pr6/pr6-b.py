# Write a Python program to read last n lines of a file

def read_last_line(file, n):
    with open(file, 'r') as f:
        line = f.readlines()
        print(line[-n:])

        print("Displaying using for loop")

        for li in line[-n:]:

            '''basically how end works lol'''
            if li.endswith('\n'):
                li = li.split('\n')
                print(li[0])

            # print(li, end="")


no_lines = int(input("Enter number of lines from the last line you wish to display: "))
read_last_line('/home/criz/Documents/GitHub/spez/py-up/pract/pr6/pog.txt', no_lines)