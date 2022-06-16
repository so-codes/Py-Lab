# Implement Exception Handling

print("Testing something lul")
num = int(input("Enter a number: "))

try:
    print("{} / {} = {}".format(num, 0, num / 0))
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
except Exception:
    print("Invalid input")
except:
    print("Something went wrong")
else:
    print("No exceptions")
finally:
    print("This will run no matter what")

x = "java exception handling is better ngl"

if not type(x) is int:
  raise TypeError("Only integers are allowed") 