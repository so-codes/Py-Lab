# exception handling
x = 10/0
try:
    print(x)
except Exception as e:
    print(e)
except:
    print("Something else went wrong")