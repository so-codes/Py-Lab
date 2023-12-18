# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

def is_vowel(char):
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
        return True
    else:
        return False

char = input("Enter a character: ")
while(not char.isalpha()):
    char = input("Enter a valid character: ")

if (is_vowel(char)):
    print(char, "is a vowel")
else:
    print(char , "is a consonant")