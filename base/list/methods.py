pogList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Append
pogList.append(11)
print(pogList)

# Clear
pogList.clear()
print(pogList)

# Copy
pogList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pogList2 = pogList.copy()
print(pogList2)

# Count
pogList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(pogList.count(1))

# Extend
pogList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pogList2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pogList.extend(pogList2)
print(pogList)

# Index
pogList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(pogList.index(1))

# Insert
pogList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pogList.insert(0, 0)
print(pogList)

# Pop
pogList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pogList.pop(0)
print(pogList)

# Remove
pogList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pogList.remove(1)
print(pogList)

# Reverse
pogList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pogList.reverse()
print(pogList)

# Sort
pogList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pogList.sort()
print(pogList)

# Sort Reverse
pogList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pogList.sort(reverse=True)
print(pogList)

# Sort Key
pogList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def myfunc(n):
    return abs(n - 5)
pogList.sort(key = myfunc)
print(pogList)

# Sort Key Reverse
pogList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def myfunc(n):
    return abs(n - 5)
pogList.sort(key = myfunc, reverse=True)
print(pogList)