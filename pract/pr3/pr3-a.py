# write a function to check a sentence to see if it is a pangram or not.

def isPangram(sen):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in sen.lower():
            return False
    return True


print("Enter a sentence: ")
sentence = input()

if(isPangram(sentence)):
    print("\nThe sentence is a pangram")
else:
    print("\nThe sentence is not a pangram")