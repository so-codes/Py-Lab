# Implement Exception Handling

class Error(Exception): 
    pass
class ValueTooSmallError(Error):
    def __init__(self, arg):
       self.strerror = arg
class ValueTooLargeError(Error): # Raised when input value is too large
    def __init__(self, arg):
       self.strerror = arg
# user guesses this number
number = 15
# Looping till the number is equal
while True:
    try:
       input_num = int(input("Guess the number by entering the value: "))
       if input_num < number:
          raise ValueTooSmallError(
          "Value entered is smaller than the answer")
       elif input_num > number:
          raise ValueTooLargeError("Value entered is larger than the answer")
       else:
          break
    except ValueTooSmallError as e:
       print("Error message:", e.strerror, "\n")
    except ValueTooLargeError as e:
       print("Error message:", e.strerror, "\n")

print("Congratulations you guessed the answer!\U0001f604")