# Write a function that takes a character (i.e. a string of length 1) and returns Trueif it is a vowel, False otherwise.

def is_vowel(ch):
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        print("True")
        return True
    else:
        print("False")
        return False

char = input("Enter a character: ")

is_vowel(char)