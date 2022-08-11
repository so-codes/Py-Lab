a = "ello matey"
print(a[6])

# loop
for i in a:
    print(i, end="")
    pass

# length
lenA = len(a)
print(lenA)

# check string
print("ello" in a)

if "ello" in a:
    print("ello is in a")

if "ello" not in a:
    print("ello is not in a")

# slicing
print(a[0:6])
print(a[6:])
print(a[:6])

# string formatting
print("{} {}".format("Hello", "World"))
print("{0} {1}".format("Hello", "World"))
print("{1} {0}".format("Hello", "World"))
print("{name} {age}".format(name="John", age=30))
print("{name} {age}".format(age=30, name="John"))
print("{0} {1} {2}".format(1, 2, 3))
print("{0} {1} {2}".format(*[1, 2, 3]))
print("{0} {1} {2}".format(*(1, 2, 3)))
print("{0} {1} {2}".format(*{"0": 1, "1": 2, "2": 3}))