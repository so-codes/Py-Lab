import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed exactly 2 (any) characters, and an "o":

x = re.findall("he.{2}o", txt)

print(x)
