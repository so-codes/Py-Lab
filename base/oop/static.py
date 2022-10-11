# Class for Computer Science Student
class CSStudent:
    stream = 'cse'# Class Variable
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        

a = CSStudent('Geek', 1)
b = CSStudent('Expert', 2)

print(a.stream)  
print(b.stream) 

print(a.name)
print(b.name)

print(a.roll)
print(b.roll)

print(CSStudent.stream) 

print("=======")
b.stream = 'ece'
print(a.stream)
print(b.stream) 

print("=======")
CSStudent.stream = 'mech'
print(a.stream) 
print(b.stream) 