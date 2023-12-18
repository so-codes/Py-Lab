def arms(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        print("arms")
    else:
        print("not arms")

arms(153)

def plai(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum * 10 + digit
        temp //= 10

    if num == sum:
        print("plai")
    else:
        print("not plai")

plai(121)

def pai(num):
    if str(num) == str(num)[::-1]:
        print("pali")
    else:
        print("not pali")

pai(121)

def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num - 1)

print(fact(5)) 


def facti(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

print(facti(5))

def sumnum(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum

print(sumnum(2))


def fibo(num):
    a = 0
    b = 1
    for i in range(num):
        print(a, end=" ")
        a = b
        b = a + b

fibo(5)

n1 , n2 = 0 , 1
nterms = int(input("Enter the number of terms: "))
count = 0

while count < nterms:
    print(n1, end =" ")
    nth = n1  + n2
    n1 = n2
    n2 = nth
    count += 1

print("\n")

def pan(str):
    whole = "abcdefghijklmnopqrstuvwxyz"
    for i in whole:
        if i not in str.lower():
            return False
        
    return True

print(pan("The quick brown fox jumps"))