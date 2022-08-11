# file opeaning
f = open('./pog.txt', 'r')
print(f.read(1))

# file closing
f.close()

# file writing
f = open('./pog.txt', 'w')
f.write('Hello World')
f.close()

# file appending
f = open('./pog.txt', 'a')
f.write('Hello World')
f.close()

# file reading
f = open('./pog.txt', 'r')
print(f.read())
f.close()

# file reading line by line
f = open('./pog.txt', 'r')
for line in f:
    print(line)
f.close()

# check if file exists
import os
print(os.path.exists('./pog.txt'))

# check if file is a file
import os
print(os.path.isfile('./pog.txt'))

# check if file is a directory
import os
print(os.path.isdir('./pog.txt'))

# delete file
import os
os.remove('./pog.txt')

# get the current working directory
import os
print(os.getcwd())

# change the current working directory
import os
os.chdir('/home/user/')
print(os.getcwd())

# join and split paths
import os
print(os.path.join('/home/user/', 'pog.txt'))
print(os.path.split('/home/user/pog.txt'))

