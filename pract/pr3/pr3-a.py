# write a function to check a sentence to see if it is a pangram or not.

def isPangram(sen):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if letter not in sen.lower():
            print("\nThe sentence is not a pangram")
            return False

    print("\nThe sentence is a pangram")
    return True


print("Enter a sentence: ")
sentence = input()

isPangram(sentence)