import mod
mod.greeting("Pog")

age = mod.person["age"]
print(age)

mod.person["age"] = 21
print(mod.person["age"])

import platform
x = platform.system()
print(x)

x = dir(platform)
print("------------------------")
for stuff in x:
    if stuff.startswith("_") and stuff.endswith("_") or stuff.startswith("_") or stuff.startswith("__"):
        pass
    else:
        print(stuff)
print("------------------------")