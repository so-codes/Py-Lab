# Write a function that takes a character (i.e. a string of length 1) and returns Trueif it is a vowel, False otherwise.

char = input("Enter a character: ")
def is_vowel(char):
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        return True
    else:
        return False

while(not char.isalpha()):
    char = input("Enter a valid character: ")

if (is_vowel(char)):
    print(char, "is a vowel")
else:
    print(char , "is a consonant")