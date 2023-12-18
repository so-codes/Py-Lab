ppl = ["criz", "speedy_bat", "inforgas"]
print(ppl)

# Append
ppl.append("jim")
print(ppl)

# Copy
ppl.copy()
print(ppl)

# Count
print(ppl.count("jim")) # count the number of times jim appears in the list

# Extend
ppl.extend(["jim", "jim"])
print(ppl)

# Index
ppl.index("speedy_bat")
print(ppl)

# Insert
ppl.insert(1, "jim")
print(ppl)

# Pop
ppl.pop()
print(ppl)

# Remove
ppl.remove("speedy_bat")
print(ppl)

# Reverse
ppl.reverse()
print(ppl)

# Sort
ppl.sort()
print(ppl)

# Clear
ppl.clear()
print(ppl)
