class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def pog(self):
        print(self.fname, self.lname)

x = Person("John", "Doe")
x.pog()

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def pog(self):
        print(self.fname, self.lname, self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.pog()